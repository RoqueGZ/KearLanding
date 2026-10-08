# Validación de la versión piloto

- Instalación `tools/setup.sh`: ejecutada dos veces con lockfile congelado, sin modificar fuentes del tema.
- Arranque de ambos servicios con los scripts guardados: probado después de detener las instancias iniciales.
- GET de vista estática y WordPress: HTTP 200, H1 esperado, idioma es-AR.
- Responsive en vista estática y WordPress: 360, 390, 768 y 1440 px; sin desbordamiento horizontal.
- Vista estática: CTA antes del visual en móvil, FAQ con teclado, validación de obligatorios/teléfono/correo, estado enviando y éxito simulado, sin solicitudes externas ni transmisión de datos.
- Sin JavaScript: contenido y FAQ accesibles, envío deshabilitado. Movimiento reducido respetado.
- axe-core sobre vista estática móvil: 24 reglas aprobadas, cero infracciones detectadas, dos comprobaciones que requieren revisión humana.
- WordPress 6.8 / PHP 8.3: 175 bloques nativos válidos, cero errores de serialización. Los scripts del editor solicitan el usuario actual y reciben 401 esperado al trabajar sin autenticar; sin otros errores de scripts en esta comprobación.
- Apertura directa de HTML mediante file: bloqueada por la política del navegador cloud. El flujo mediante servidor fue validado.
- Sin brief, fotografías, videos ni referencias: su revisión y el rendimiento con medios finales quedan pendientes. Sin envío real, analítica ni despliegue.

Capturas y detalles técnicos locales: `sitio/.local/checks/` (excluidos de los paquetes de entrega). Las comprobaciones automáticas no certifican conformidad total de accesibilidad ni validez comercial del contenido propuesto.
