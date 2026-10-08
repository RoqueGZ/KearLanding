"""Generate static preview from the actual WordPress pattern and template parts."""
from pathlib import Path
import re, shutil
root = Path(__file__).resolve().parents[1]
theme, out = root/'kear-landings', root/'preview'
out.mkdir(exist_ok=True)
def read(path):
    value = path.read_text()
    value = re.sub(r'<\?php.*?\?>', '', value, flags=re.S)
    return re.sub(r'<!--\s*/?wp:.*?-->', '', value, flags=re.S)
body = '<a class="skip-link" href="#contenido">Saltar al contenido</a><header>'+read(theme/'parts/header.html')+'</header><main id="contenido">'+read(theme/'patterns/landing-electrica.php')+'</main><footer>'+read(theme/'parts/footer.html')+'</footer>'
(out/'index.html').write_text('''<!doctype html>
<html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Instalaciones eléctricas para empresas en Santa Fe | KEAR</title>
<meta name="description" content="Instalaciones eléctricas, tableros y automatización para empresas en Santa Fe. Contanos tu proyecto y consultá por WhatsApp o formulario.">
<meta name="robots" content="noindex, nofollow">
<link rel="stylesheet" href="../kear-landings/style.css"><script src="../kear-landings/assets/landing.js" defer></script>
</head><body>'''+body+'</body></html>')
print('Vista generada: sitio/preview/index.html')
