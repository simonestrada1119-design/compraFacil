document.addEventListener('DOMContentLoaded', function () {
    // Validaciones para Formulario de Proveedor
    const proveedorForm = document.querySelector('form[action*="proveedor"]');
    if (proveedorForm) {
        proveedorForm.addEventListener('submit', function (e) {
            let esValido = true;

            const razonSocial = document.getElementById('id_razon_social');
            const nit = document.getElementById('id_nit');
            const telefono = document.getElementById('id_telefono');
            const correo = document.getElementById('id_correo');
            const direccion = document.getElementById('id_direccion');

            // Limpiar errores previos
            document.querySelectorAll('.invalid-feedback').forEach(el => el.remove());
            document.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));

            function mostrarError(campo, mensaje) {
                campo.classList.add('is-invalid');
                const feedback = document.createElement('div');
                feedback.className = 'invalid-feedback';
                feedback.innerText = mensaje;
                campo.parentNode.appendChild(feedback);
                esValido = false;
            }

            if (razonSocial && !razonSocial.value.trim()) {
                mostrarError(razonSocial, 'El nombre o razón social es obligatorio.');
            }
            if (nit && !nit.value.trim()) {
                mostrarError(nit, 'El NIT es obligatorio.');
            }
            if (telefono && !/^[0-9+\s()-]+$/.test(telefono.value.trim())) {
                mostrarError(telefono, 'Ingrese un teléfono válido (solo números y caracteres permitidos).');
            }
            if (correo && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(correo.value.trim())) {
                mostrarError(correo, 'Ingrese un correo electrónico válido.');
            }
            if (direccion && !direccion.value.trim()) {
                mostrarError(direccion, 'La dirección es obligatoria.');
            }

            if (!esValido) {
                e.preventDefault();
            }
        });
    }

    // Validaciones para Formulario de Compra
    const compraForm = document.querySelector('form[action*="compra"]');
    if (compraForm) {
        compraForm.addEventListener('submit', function (e) {
            let esValido = true;

            const numCompra = document.getElementById('id_numero_compra');
            const proveedor = document.getElementById('id_proveedor');
            const fecha = document.getElementById('id_fecha_compra');
            const descripcion = document.getElementById('id_descripcion');
            const valor = document.getElementById('id_valor_total');

            document.querySelectorAll('.invalid-feedback').forEach(el => el.remove());
            document.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));

            function mostrarError(campo, mensaje) {
                campo.classList.add('is-invalid');
                const feedback = document.createElement('div');
                feedback.className = 'invalid-feedback';
                feedback.innerText = mensaje;
                campo.parentNode.appendChild(feedback);
                esValido = false;
            }

            if (numCompra && !numCompra.value.trim()) {
                mostrarError(numCompra, 'El número de compra es obligatorio.');
            }
            if (proveedor && !proveedor.value) {
                mostrarError(proveedor, 'Debe seleccionar un proveedor.');
            }
            if (fecha && !fecha.value) {
                mostrarError(fecha, 'La fecha de compra es obligatoria.');
            }
            if (descripcion && !descripcion.value.trim()) {
                mostrarError(descripcion, 'La descripción es obligatoria.');
            }
            if (valor && (isNaN(valor.value) || parseFloat(valor.value) <= 0)) {
                mostrarError(valor, 'El valor total debe ser un número mayor que cero.');
            }

            if (!esValido) {
                e.preventDefault();
            }
        });
    }
});