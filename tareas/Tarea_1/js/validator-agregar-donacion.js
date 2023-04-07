// Validacion de formulario

const validarForm = () => {

  // Fecha actual
  const fechaActual = new Date().toISOString().slice(0,10);

  // Fotos

  // Expresiones regulares
  const emailExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const celularExp = /^$|^[0-9]{10}$/;
  const formatoFecha = /^\d{4}-\d{2}-\d{2}$/;

  // Funciones auxiliares
  const validadorSelect = (opcion) => opcion!=-1;
  const validadorCalleNumero = (direccion) => direccion;
  const validadorCantidad = (cantidad) => cantidad;
  const validadorFecha = (fecha) => fecha >= fechaActual && formatoFecha.test(fecha);
  const validadorFoto = (foto) => foto; // MODIFICAR Mínimo 1, máximo 3.
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
  let fotoInput = document.getElementById("foto-1");
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

  if (!validadorFoto(fotoInput.value)) {
    msg += "Foto mala!\n";
    fotoInput.style.borderColor = "red"; // Cambiar estilo con JS!!
  } else {
    fotoInput.style.borderColor = "";
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