let cond = false;
const verFoto = () => {
    const foto = document.getElementById("foto");
    if(!cond) {
        foto.style.width = "1280px";
        foto.style.height = "1024px";
        cond = true;
    } else {
        foto.style.width = "640px";
        foto.style.height = "480px";
        cond = false;
    }
};