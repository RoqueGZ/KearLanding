"""Validate native block serialization against the installed WordPress scripts."""
from playwright.sync_api import sync_playwright
from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
helper=root/'.local/WordPress-6.8/kear-block-check.php'
assert not helper.exists(), 'Refusing to overwrite an existing local helper'
helper.write_text('''<?php require __DIR__ . '/wp-load.php'; ?>
<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Local block validation</title>
<?php wp_enqueue_script('wp-block-library'); wp_print_scripts(); ?></head><body><p>Local block validation</p></body></html>''')
try:
 with sync_playwright() as pw:
  browser=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  page=browser.new_page()
  errors=[];responses=[]
  page.on('pageerror',lambda error:errors.append(str(error)))
  page.on('response',lambda response:responses.append((response.status,response.url)))
  page.goto('http://127.0.0.1:9400/kear-block-check.php',wait_until='networkidle')
  page.evaluate('wp.blockLibrary.registerCoreBlocks()')
  invalid=[];count=0
  for file in ['patterns/landing-electrica.php','parts/header.html','parts/footer.html']:
   source=re.sub(r'<\?php.*?\?>','',(root/'kear-landings'/file).read_text(),flags=re.S)
   result=page.evaluate('''source=>{let count=0,invalid=[];const blocks=wp.blocks.parse(source);function visit(items){for(const b of items){count++;if(!b.isValid)invalid.push({name:b.name,attributes:b.attributes,original:b.originalContent,expected:wp.blocks.getSaveContent(b.name,b.attributes,b.innerBlocks)});visit(b.innerBlocks)}}visit(blocks);return {count,invalid}}''',source)
   count+=result['count']
   invalid.extend([{'file':file,**i} for i in result['invalid']])
  # Core editor scripts request the current user even when only parsing blocks.
  # This logged-out diagnostic intentionally uses no credentials.
  expected_401=any(status==401 and '/wp-json/wp/v2/users/me' in url for status,url in responses)
  unexpected=[error for error in errors if not (error=='Object' and expected_401)]
  report={'native_blocks':count,'invalid_blocks':invalid,'expected_logged_out_editor_api_401':expected_401,'unexpected_script_errors':unexpected}
  (root/'.local/checks').mkdir(exist_ok=True)
  (root/'.local/checks/blocks-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
  print(json.dumps(report,ensure_ascii=False,indent=2))
  browser.close()
  assert not unexpected,unexpected
  assert not invalid,f'{len(invalid)} invalid blocks'
finally:
 helper.unlink()
