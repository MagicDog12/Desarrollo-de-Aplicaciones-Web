// Validacion de formulario

const validarForm = () => {

    // Expresiones regulares
    const emailExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const celularExp = /^$|^[0-9]{10}$/;
    // Funciones auxiliares
    const validadorSelect = (opcion) => opcion!=-1;
    const validadorDescripcion = (descripcion) => descripcion && descripcion.length <=250;
    const validadorCantidad = (cantidad) => cantidad;
    const validadorNombre = (nombre) => nombre && nombre.length >= 3 && nombre.length <= 80;
    const validadorEmail = (email) => email && emailExp.test(email);
    const validadorCelular = (celular) => celularExp.test(celular);

    // Obtener el formulario del DOM por el ID
    // let form = document.getElementById("formulario");

    // Obtener inputs del DOM por el ID
    let regionInput = document.getElementById("region");
    let comunaInput = document.getElementById("comuna");
    let tipoInput = document.getElementById("tipo");
    let descripcionInput = document.getElementById("descripcion");
    let cantidadInput = document.getElementById("cantidad");
    let nombreInput = document.getElementById("nombre");
    let emailInput = document.getElementById("email");
    let celularInput = document.getElementById("celular");

    let isValid = false;
    let msg = "";

    if (!validadorSelect(regionInput.value)) {
        msg += "Region mala!\n";
        regionInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        regionInput.style.borderColor = "";
    }

    if (!validadorSelect(comunaInput.value)) {
        msg += "Comuna mala!\n";
        comunaInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        comunaInput.style.borderColor = "";
    }

    if (!validadorSelect(tipoInput.value)) {
        msg += "Tipo malo!\n";
        tipoInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        tipoInput.style.borderColor = "";
    }

    if (!validadorDescripcion(descripcionInput.value)) {
        msg += "Descripcion mala!\n";
        descripcionInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        descripcionInput.style.borderColor = "";
    }

    if (!validadorCantidad(cantidadInput.value)) {
        msg += "Cantidad mala!\n";
        cantidadInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        cantidadInput.style.borderColor = "";
    }

    if (!validadorNombre(nombreInput.value)) {
        msg += "Nombre malo!\n";
        nombreInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        nombreInput.style.borderColor = "";
    }

    if (!validadorEmail(emailInput.value)) {
        msg += "Email malo!\n";
        emailInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        emailInput.style.borderColor = "";
    }

    if (!validadorCelular(celularInput.value)) {
        msg += "Celular malo!\n";
        celularInput.style.borderColor = "red"; // Cambiar estilo con JS!!
    } else {
        celularInput.style.borderColor = "";
    }

    if(msg === "") {
        msg = "Felicitaciones, tu formulario ha sido enviado";
        isValid = true;
        // form.submit();

        // No contamos con un backend, asi que de momento
        // utilizaremos el localStorage para dar la 
        // sensacion de que hemos enviado el formulario.
        let nombre = nombreInput.value;
        localStorage.setItem("nombre", nombre);
    }
    alert(msg); // Alertas de JS

    if (isValid) {
        window.location.href = "./inicio.html";
    }
};

// Recuperamos el boton que envia el formulario
let submitBtn = document.getElementById("envio");
submitBtn.addEventListener("click", validarForm);