# KEAR Instalaciones · landing piloto

Primera versión local de la landing B2B para instalaciones eléctricas en Santa Fe. Tema de bloques nativo de WordPress, sin Elementor, dependencias comerciales, envío de datos ni despliegue.

**Material disponible:** únicamente el pedido adjunto. El checkout estaba vacío. No se recibieron `/brief`, `/assets-kear` ni `/referencias/pinterest`. Todo el copy complementario es **TEXTO PROPUESTO**, no contenido aprobado del brief. No se utilizaron fotos ni videos, y no se atribuyeron clientes, resultados o características técnicas a trabajos.

## Descargar desde GitHub

En la rama `codex/kear-piloto` están el [proyecto completo](sitio/kear-piloto.zip) y el [tema WordPress](sitio/kear-landings.zip). Abrí el archivo ZIP en GitHub y usá **Download raw file**. También podés descargar la rama desde **Code → Download ZIP**. El código y la vista generada se incluyen; las herramientas instaladas y los datos locales de WordPress quedan excluidos.

## Abrir la propuesta

Desde la carpeta del proyecto:

```bash
bash sitio/tools/start-preview.sh
```

El servidor muestra la carpeta `sitio`. En un navegador de tu propia máquina, abrí la ruta `/preview/` del servidor en el puerto **4173**. El HTML generado está en `sitio/preview/index.html`, con recursos locales y rutas relativas. Usá el servidor para abrirlo: la política del navegador del entorno cloud bloquea la apertura directa de archivos y esa vía no pudo validarse aquí. En este onboarding, el servidor se usa para comprobaciones internas; la interfaz no proporciona una vista web de localhost.

La vista se genera desde el patrón y las partes del tema. Tras editar esos archivos, ejecutá de nuevo el generador. No edites la vista generada.

## WordPress local

Requiere Node >=24.18 y Python 3. Se usa WordPress Playground con PHP 8.3 y SQLite local. No requiere PHP, MySQL, Hostinger ni autenticación remota.

```bash
bash sitio/tools/setup.sh
bash sitio/tools/start-wordpress.sh
```

WordPress usa el puerto **9400**. El tema queda activado automáticamente. Las herramientas y la instalación local viven en `sitio/.local/`, ignorada por Git. Los comandos de arranque mantienen el servidor en primer plano; para detenerlo, usá Ctrl+C. Usá terminales distintas para ambas vistas. No se crean worktrees.

WordPress 6.8 se fijó para esta prueba aislada; antes de un despliegue futuro se debe elegir y probar la versión estable vigente. Esta instalación de desarrollo no es un servicio de producción ni debe exponerse públicamente.

## Archivos

- `sitio/kear-landings/style.css`: identidad del tema, diseño responsive y estados interactivos.
- `sitio/kear-landings/theme.json`: paleta, tipografía y configuración del editor.
- `sitio/kear-landings/functions.php`: recursos, registro de patrones, accesibilidad y SEO provisional.
- `sitio/kear-landings/templates/{front-page,index,page}.html`: plantillas nativas.
- `sitio/kear-landings/parts/{header,footer}.html`: navegación, contacto y privacidad editables.
- `sitio/kear-landings/patterns/landing-electrica.php`: las nueve secciones de contenido; el footer completa contacto y privacidad.
- `sitio/kear-landings/assets/landing.js`: demostración del formulario; no usa fetch, almacenamiento ni analítica.
- `sitio/kear-landings/assets/inter-*.woff2` y `Inter-LICENSE.txt`: Inter 400/600/700 autoalojada, licencia OFL.
- `sitio/tools/preview.py`: genera `sitio/preview/index.html` desde el tema.
- `sitio/tools/{setup,start-preview,start-wordpress}.sh`: instalación y arranque repetibles.
- `sitio/tools/{package.json,package-lock.json,wordpress-blueprint.json}`: herramientas fijadas y activación local.
- `sitio/tools/check_*.py`: comprobaciones funcionales, accesibilidad y serialización de bloques.
- `sitio/CONTENIDO-PENDIENTE.md`: lista de validaciones y materiales necesarios.

## Edición y reutilización

Hero, servicios, casos, proceso, empresa, FAQ y CTA usan bloques nativos editables. El formulario demostrativo usa un bloque HTML. Se puede insertar el patrón **KEAR · Instalaciones eléctricas para empresas** en una página usando la plantilla `page`; las demás landings podrán tener sus propios patrones y reutilizar paleta, partes y estilos.

El patrón incluido en `front-page` define la portada piloto. El editor de sitio permite modificar la portada y las partes; los cambios del editor se guardan en la base de datos y tienen prioridad sobre los archivos del tema. La vista estática refleja exclusivamente los archivos. No exporta cambios de la base de datos.

Los CTA de WhatsApp llevan a `#contacto`, con aviso explícito de número pendiente. Sustituir sus destinos por la URL aprobada es una tarea posterior de contenido. Las fotografías pendientes son grupos visuales editables, preparados para sustituirse por bloques Imagen reales con alt, proporción, tamaños responsive y lazy loading fuera del hero.

Title/meta son provisionales en `functions.php` y la vista. En la integración futura, centralizarlos en el sistema SEO de WordPress para evitar duplicados. La vista estática incluye `noindex`; WordPress local tiene `blog_public=0`.

## Comprobaciones

La vista local se comprobó a 360, 390, 768 y 1440 px: sin desbordamiento, con CTA antes de la imagen en móvil, controles táctiles, FAQ con teclado, errores y estados de envío simulado, movimiento reducido y contenido/FAQ disponibles sin JavaScript. El formulario está deshabilitado sin JS para impedir un envío accidental.

Se usa Chromium y Python Playwright para las comprobaciones; ya están disponibles en este entorno. Las pruebas de accesibilidad usan axe-core local, instalado por `setup.sh`. La comprobación de bloques requiere WordPress local y un archivo auxiliar temporal en la instalación de pruebas. No autentica usuarios ni altera contenido comercial.

```bash
python3 sitio/tools/check_preview.py
python3 sitio/tools/check_accessibility.py
python3 sitio/tools/check_wordpress.py
```

Las capturas y reportes se guardan en `sitio/.local/checks/`. Las pruebas automáticas no reemplazan una revisión humana de copy, fotografía, contraste sobre imágenes finales ni una sesión con lector de pantalla.

## Dirección visual y segunda iteración

Composición editorial, grandes titulares Inter, mucho espacio blanco, paneles carbón con trama técnica discreta, tarjetas pequeñas superpuestas y verde #176B45 para las acciones. El panel gráfico del hero señala material pendiente; no simula una obra real. No se incorporó un color de marca adicional, video, carrusel ni animaciones continuas.

Prioridades siguientes: incorporar el brief aprobado y las fotos reales; completar dos casos con datos autorizados; confirmar contactos, carácter familiar y privacidad; conectar el formulario mediante un procedimiento separado y validar consentimiento/antispam; verificar rendimiento con las imágenes finales y medir consultas, distinguiendo clics de WhatsApp de ventas. Sin cifras, promesas ni cobertura nacional irrestricta.
