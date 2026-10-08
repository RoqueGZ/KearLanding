from playwright.sync_api import sync_playwright
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':390,'height':844})
    page.goto('http://127.0.0.1:4173/preview/')
    page.add_script_tag(path=str(root/'.local/runtime/node_modules/axe-core/axe.min.js'))
    result=page.evaluate('async()=>await axe.run(document,{runOnly:{type:"tag",values:["wcag2a","wcag2aa","wcag21aa"]}})')
    violations=[{'id':v['id'],'impact':v['impact'],'nodes':[n['target'] for n in v['nodes']]} for v in result['violations']]
    print(json.dumps({'violations':violations,'passed_rules':len(result['passes']),'manual_review_rules':len(result['incomplete'])},indent=2))
    browser.close()
    assert not violations
