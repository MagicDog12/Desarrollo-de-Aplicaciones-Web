let selectRegiones = document.getElementById("region");
let selectComunas = document.getElementById("comuna");

fetch("../static/otros/region_comuna.json")
    .then(Response => Response.json())
    .then(contenido => {

        let llenarRegiones = () => {
            for (let reg of contenido.regiones) {
                let option = document.createElement("option");
                option.text = reg.nombre;
                selectRegiones.add(option);
            }
        };

        let llenarComunas = () => {
            selectComunas.innerHTML = "";
            let regionSeleccionada = selectRegiones.value;
            for (let reg of contenido.regiones) {
                if (reg.nombre === regionSeleccionada) {
                    for (let com of reg.comunas) {
                        let option = document.createElement("option");
                        option.text = com.nombre;
                        selectComunas.add(option);
                    }
                break;
                }
            }
        };

        selectRegiones.addEventListener("change", llenarComunas);
        llenarRegiones();
    })
    .catch(error => console.error(error));


  