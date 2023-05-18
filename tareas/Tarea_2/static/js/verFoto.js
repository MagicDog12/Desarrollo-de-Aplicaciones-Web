
const verFoto = () => {
    const fotos = document.getElementsByClassName("foto");
    for(let i = 0; i < fotos.length; i++) {
        let foto = fotos[i];
        if(foto.style.width == "640px") {
            foto.style.width = "1280px";
            foto.style.height = "1024px";
        } else {
            foto.style.width = "640px";
            foto.style.height = "480px";
        }
    }
};