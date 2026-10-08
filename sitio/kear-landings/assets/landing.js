/* Local demonstration only: no request, storage, analytics or WhatsApp destination. */
(() => {
  const form = document.querySelector('#kear-form');
  if (!form) return;
  const button = form.querySelector('button[type="submit"]');
  const status = form.querySelector('#form-status');
  button.disabled = false;
  const fields = [...form.querySelectorAll('input, textarea')];
  function errorFor(field) {
    if (field.required && !field.value.trim()) return 'Completá este campo para continuar.';
    if (field.type === 'email' && field.value && !field.validity.valid) return 'Revisá el formato del correo electrónico.';
    if (field.type === 'tel' && field.value && !/^[+()\d\s.-]{6,40}$/.test(field.value.trim())) return 'Ingresá un teléfono con al menos 6 caracteres válidos.';
    return '';
  }
  function validate(field) {
    const message = errorFor(field);
    const error = document.getElementById(`${field.id}-error`);
    if (error) error.textContent = message;
    if (message) field.setAttribute('aria-invalid', 'true');
    else field.removeAttribute('aria-invalid');
    return !message;
  }
  fields.forEach(field => field.addEventListener('input', () => {
    if (field.hasAttribute('aria-invalid')) validate(field);
    status.textContent = '';
    status.classList.remove('success');
  }));
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (button.disabled) return;
    const invalid = fields.filter(field => !validate(field));
    status.classList.remove('success');
    if (invalid.length) {
      status.textContent = 'Revisá los campos indicados. No se envió información.';
      invalid[0].focus();
      return;
    }
    button.disabled = true;
    form.setAttribute('aria-busy', 'true');
    button.textContent = 'Enviando…';
    status.textContent = 'Simulando el envío. No se transmite información.';
    window.setTimeout(() => {
      status.textContent = 'Demostración completada. Tus datos no fueron enviados ni guardados.';
      status.classList.add('success');
      button.textContent = 'Enviar consulta';
      button.disabled = false;
      form.removeAttribute('aria-busy');
    }, 900);
  });
})();
