from pathlib import Path
from playwright.sync_api import sync_playwright
import json
root=Path(__file__).resolve().parents[1]
out=root/'.local/checks'
out.mkdir(parents=True,exist_ok=True)
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    page=browser.new_page()
    errors=[]
    page.on('pageerror',lambda error: errors.append(str(error)))
    requests=[]
    page.on('request',lambda req: requests.append((req.method,req.url)))
    for width in [360,390,768,1440]:
        page.set_viewport_size({'width':width,'height':900})
        page.goto('http://127.0.0.1:4173/preview/',wait_until='networkidle')
        assert page.locator('h1').count()==1
        assert page.locator('section').count()==9
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),f'Overflow at {width}'
        assert page.locator('h1').inner_text().startswith('Instalaciones eléctricas integrales')
        if width < 768:
            assert page.locator('.hero .wp-block-button__link').bounding_box()['y'] < page.locator('.hero-media').bounding_box()['y']
        assert page.locator('.wp-block-button__link').first.bounding_box()['height']>=48
        page.screenshot(path=str(out/f'preview-{width}.png'),full_page=True)
    page.locator('summary').first.focus()
    page.keyboard.press('Enter')
    assert page.locator('details').first.get_attribute('open') is not None
    page.locator('a[href="#consulta"]').first.click()
    assert page.url.endswith('#consulta')
    form=page.locator('#kear-form')
    form.locator('button').click()
    assert page.locator('[aria-invalid="true"]').count()==4
    assert page.evaluate('document.activeElement.id')=='nombre'
    page.locator('#nombre').fill('Prueba local')
    page.locator('#telefono').fill('abcdef')
    page.locator('#localidad').fill('Nelson, Santa Fe')
    page.locator('#necesidad').fill('Datos ficticios para comprobar el formulario')
    form.locator('button').click()
    assert page.locator('#telefono').get_attribute('aria-invalid')=='true'
    page.locator('#telefono').fill('0342 1234567')
    page.locator('#email').fill('invalido')
    form.locator('button').click()
    assert page.locator('#email').get_attribute('aria-invalid')=='true'
    page.locator('#email').fill('prueba@example.com')
    form.locator('button').click()
    assert form.get_attribute('aria-busy')=='true'
    assert form.locator('button').is_disabled()
    page.wait_for_function("document.querySelector('#form-status').classList.contains('success')")
    assert 'no fueron enviados' in page.locator('#form-status').inner_text()
    assert not any(method != 'GET' or not url.startswith('http://127.0.0.1:4173/') for method,url in requests)
    assert not errors,errors
    page.emulate_media(reduced_motion='reduce')
    assert page.evaluate('getComputedStyle(document.documentElement).scrollBehavior')=='auto'
    nojs=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':900})
    np=nojs.new_page();np.goto('http://127.0.0.1:4173/preview/')
    assert np.locator('h1').is_visible()
    np.locator('summary').first.click()
    assert np.locator('details').first.get_attribute('open') is not None
    assert np.locator('#kear-form button').is_disabled()
    browser.close()
print(json.dumps({'responsive':[360,390,768,1440],'horizontal_overflow':False,'faq_keyboard':'passed','form':['required','phone','email','sending','demo_success'],'external_requests':0,'javascript_errors':errors,'no_javascript':'content and FAQ available; sending disabled','reduced_motion':'passed'},ensure_ascii=False,indent=2))
