// Validacion de formulario

const validarForm = () => {

    // Expresiones regulares
    const emailExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const celularExp = /^$|^9\d{8}$/;
    // Funciones auxiliares
    const validadorSelect = (opcion) => opcion;
    const validadorDescripcion = (descripcion) => descripcion && descripcion.length <=250;
    const validadorCantidad = (cantidad) => cantidad;
    const validadorNombre = (nombre) => nombre && nombre.length >= 3 && nombre.length <= 80;
    const validadorEmail = (email) => email && emailExp.test(email);
    const validadorCelular = (celular) => celularExp.test(celular);

    // Obtener inputs del DOM por el ID
    let regionInput = document.getElementById("region");
    let comunaInput = document.getElementById("comuna");
    let tipoInput = document.getElementById("tipo");
    let descripcionInput = document.getElementById("descripcion");
    let cantidadInput = document.getElementById("cantidad");
    let nombreInput = document.getElementById("nombre");
    let emailInput = document.getElementById("email");
    let celularInput = document.getElementById("celular");

    let msg = "";

    if (!validadorSelect(regionInput.value)) {
        msg += "Selecciona una región<br>";
        regionInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        regionInput.style.borderColor = "";
    }

    if (!validadorSelect(comunaInput.value)) {
        msg += "Selecciona una comuna <br>";
        comunaInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        comunaInput.style.borderColor = "";
    }

    if (!validadorSelect(tipoInput.value)) {
        msg += "Selecciona un tipo <br>";
        tipoInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        tipoInput.style.borderColor = "";
    }

    if (!validadorDescripcion(descripcionInput.value)) {
        msg += "Ingresa una descripción de máximo 250 carácteres <br>";
        descripcionInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        descripcionInput.style.borderColor = "";
    }

    if (!validadorCantidad(cantidadInput.value)) {
        msg += "Ingresa una cantidad <br>";
        cantidadInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        cantidadInput.style.borderColor = "";
    }

    if (!validadorNombre(nombreInput.value)) {
        msg += "Ingresa el nombre del solicitante, mínimo 3 carácteres y máximo 80 <br>";
        nombreInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        nombreInput.style.borderColor = "";
    }

    if (!validadorEmail(emailInput.value)) {
        msg += "Ingresa una dirección de correo válida en formato abc@def.ghi <br>";
        emailInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        emailInput.style.borderColor = "";
    }

    if (!validadorCelular(celularInput.value)) {
        msg += "Ingresa un número de celular válido en formato 912345678 (recuerda que comienza con 9) <br>";
        celularInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        celularInput.style.borderColor = "";
    }

    const alertPlaceholder = document.getElementById('liveAlertPlaceholder');

    const regresar = () => {
        window.location.href = "/";
    }

    const ir = () => {
        let form = document.querySelector("form");
        let data = new FormData(form);

        fetch("/agregar-pedido", {
            method: "POST",
            body: data
        }).then(function(response) {
            alertPlaceholder.innerHTML = [
                `<div class="alert alert-success alert-dismissible" role="alert">`,
                `   <div>Hemos recibido la información de su pedido. Muchas gracias.</div>`,
                '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
                '</div>'
                ].join('');
                const finalBtn = document.getElementById("envio");
                finalBtn.classList.remove('btn-outline-success');
                finalBtn.classList.add('btn-outline-info')
                finalBtn.innerText = "Volver a la portada";
                finalBtn.addEventListener("click", regresar);
        });
    };
    const appendAlert = (message, type, dismissible) => {
        if(dismissible){
            alertPlaceholder.innerHTML = [
                `<div class="alert alert-${type} alert-dismissible" role="alert">`,
                `   <div>${message}</div>`,
                '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
                '</div>'
              ].join('');
        } else {
            alertPlaceholder.innerHTML = [
                `<div class="alert alert-${type} alert-dismissible" role="alert">`,
                `   <div>${message}</div>`,
                '   <button id="confirmacion" type="button" class="btn btn-success mb-3">Sí, confirmo</button>',
                '   <button type="button" class="btn btn-danger mb-3" data-bs-dismiss="alert">No, quiero volver al formulario</button>',
                '</div>'
              ].join('');
              let confirmBtn = document.getElementById("confirmacion");
              confirmBtn.addEventListener("click", ir);
        }
    }

    if(msg === "") {
        msg = "¿Confirma que desea agregar este pedido?";
        appendAlert(msg, 'success', false);
    } else {
        appendAlert(msg, 'danger', true);
    }
};
// Recuperamos el boton que envia el formulario
let submitBtn = document.getElementById("envio");
submitBtn.addEventListener("click", validarForm);
