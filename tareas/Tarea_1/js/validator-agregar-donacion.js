// Validacion de formulario

const validarForm = () => {

  // Fecha actual
  const fechaActual = new Date().toISOString().slice(0,10);

  // Expresiones regulares
  const emailExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const celularExp = /^$|^[0-9]{10}$/;
  const formatoFecha = /^\d{4}-\d{2}-\d{2}$/;

  // Funciones auxiliares
  const validadorSelect = (opcion) => opcion!=-1;
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

  if (!validadorCalleNumero(calleNumeroInput.value)) {
    msg += "Calle y número malo!\n";
    calleNumeroInput.style.borderColor = "red"; // Cambiar estilo con JS!!
  } else {
    calleNumeroInput.style.borderColor = "";
  }

  if (!validadorSelect(tipoInput.value)) {
      msg += "Tipo malo!\n";
      tipoInput.style.borderColor = "red"; // Cambiar estilo con JS!!
  } else {
      tipoInput.style.borderColor = "";
  }

  if (!validadorCantidad(cantidadInput.value)) {
      msg += "Cantidad mala!\n";
      cantidadInput.style.borderColor = "red"; // Cambiar estilo con JS!!
  } else {
      cantidadInput.style.borderColor = "";
  }

  if (!validadorFecha(fechaInput.value)) {
    msg += "Fecha mala!\n";
    fechaInput.style.borderColor = "red"; // Cambiar estilo con JS!!
  } else {
    fechaInput.style.borderColor = "";
  }

  if (!validadorFoto(fotosInput)) {
    msg += "Foto mala!\n";
    fotosInput.forEach(foto => {
        foto.style.borderColor = "red";
    });
  } else {
    fotosInput.forEach(foto => {
        foto.style.borderColor = "";
    });
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

  const alertPlaceholder = document.getElementById('liveAlertPlaceholder');

    const regresar = () => {
        window.location.href = "./inicio.html";
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