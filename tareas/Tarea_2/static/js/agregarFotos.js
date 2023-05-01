let numFotos = 2;

const agregarFoto = () => {
    if (numFotos < 4) {
        // Agregamos el input
        const input = document.createElement("input");
        input.classList.add("form-control");
        input.addEventListener("click", agregarFoto);
        input.type = "file";
        input.name = "foto-" + numFotos;
        input.id = "foto-" + numFotos;

        // Agregamos el label
        const label = document.createElement("label");
        label.classList.add("input-group-text");
        label.setAttribute("for", input.id);
        label.textContent = "Foto Donación " + numFotos;

        // Agregamos el div
        const div = document.createElement("div");
        div.classList.add("input-group");
        div.classList.add("col-md-12");
        div.id = "foto-div-" + numFotos;

        const refElement = document.querySelector("#foto-div-" + (numFotos-1));
        refElement.parentNode.insertBefore(div, refElement.nextElementSibling);
        document.querySelector("#foto-div-" + numFotos).appendChild(label);
        document.querySelector("#foto-div-" + numFotos).appendChild(input);
        numFotos++;
    }
}