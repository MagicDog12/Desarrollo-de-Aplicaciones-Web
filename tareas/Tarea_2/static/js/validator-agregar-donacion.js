// Validacion de formulario

const validarForm = () => {

  // Fecha actual
  const fechaActual = new Date().toISOString().slice(0,10);

  // Expresiones regulares
  const emailExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const celularExp = /^$|^9\d{8}$/;
  const formatoFecha = /^\d{4}-\d{2}-\d{2}$/;

  // Funciones auxiliares
  const validadorSelect = (opcion) => opcion;
  const validadorCalleNumero = (direccion) => direccion;
  const validadorCantidad = (cantidad) => cantidad;
  const validadorFecha = (fecha) => fecha >= fechaActual && formatoFecha.test(fecha);
  const validadorFoto = (fotos) => {
    const numFotos = fotos.filter(foto => foto.files.length > 0).length;
    return numFotos >= 1 && numFotos <= 3;
  }; // MODIFICAR Mínimo 1, máximo 3.
  const validadorNombre = (nombre) => nombre && nombre.length >= 3 && nombre.length <= 80;
  const validadorEmail = (email) => email && emailExp.test(email);
  const validadorCelular = (celular) => celularExp.test(celular);

  // Obtener el formulario del DOM por el ID
  // let form = document.getElementById("formulario");

  // Obtener inputs del DOM por el ID
  let regionInput = document.getElementById("region");
  let comunaInput = document.getElementById("comuna");
  let calleNumeroInput = document.getElementById("calle-numero");
  let tipoInput = document.getElementById("tipo");
  let cantidadInput = document.getElementById("cantidad");
  let fechaInput = document.getElementById("fecha-disponibilidad");
  const fotosInput = [...document.querySelectorAll('input[name^="foto-"]')];
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

  if (!validadorCalleNumero(calleNumeroInput.value)) {
    msg += "Ingresa una calle y número <br>";
    calleNumeroInput.style.borderColor = "red"; // Cambiar estilo con JS!!
  } else {
    calleNumeroInput.style.borderColor = "";
  }

  if (!validadorSelect(tipoInput.value)) {
      msg += "Selecciona un tipo <br>";
      tipoInput.style.borderColor = "red"; // Cambiar estilo con JS!!
  } else {
      tipoInput.style.borderColor = "";
  }

  if (!validadorCantidad(cantidadInput.value)) {
      msg += "Ingresa una cantidad <br>";
      cantidadInput.style.borderColor = "red"; // Cambiar estilo con JS!!
  } else {
      cantidadInput.style.borderColor = "";
  }

  if (!validadorFecha(fechaInput.value)) {
    msg += "Ingresa una fecha en formato año-mes-día que sea mayor o igual a la fecha actual <br>";
    fechaInput.style.borderColor = "red"; // Cambiar estilo con JS!!
  } else {
    fechaInput.style.borderColor = "";
  }

  if (!validadorFoto(fotosInput)) {
    msg += "Ingresa al menos 1 foto y máximo 3 fotos <br>";
    fotosInput.forEach(foto => {
        foto.style.borderColor = "red";
    });
  } else {
    fotosInput.forEach(foto => {
        foto.style.borderColor = "";
    });
  }

  if (!validadorNombre(nombreInput.value)) {
      msg += "Ingresa el nombre del donante, mínimo 3 carácteres y máximo 80 <br>";
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
        alertPlaceholder.innerHTML = [
            `<div class="alert alert-success alert-dismissible" role="alert">`,
            `   <div>Hemos recibido la información de su donación. Muchas gracias.</div>`,
            '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
            '</div>'
            ].join('');
            const finalBtn = document.getElementById("envio");
            finalBtn.classList.remove('btn-outline-success');
            finalBtn.classList.add('btn-outline-info')
            finalBtn.innerText = "Volver a la portada";
            finalBtn.addEventListener("click", regresar);
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
        msg = "¿Confirma que desea agregar esta donación?";
        appendAlert(msg, 'success', false);
    } else {
        appendAlert(msg, 'danger', true);
    }
};

// Recuperamos el boton que envia el formulario
let submitBtn = document.getElementById("envio");
submitBtn.addEventListener("click", validarForm);