
const verFoto = () => {
    const foto = document.getElementById("foto");
    if(foto.style.width == "640px") {
        foto.style.width = "1280px";
        foto.style.height = "1024px";
    } else {
        foto.style.width = "640px";
        foto.style.height = "480px";
    }
};