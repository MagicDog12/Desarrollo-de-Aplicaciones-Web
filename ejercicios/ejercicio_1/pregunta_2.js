// se buscan los elementos necesarios
let count = document.getElementById('contador'); // contador
let btnResta = document.getElementById('btn-resta'); // resta
let btnSuma = document.getElementById('btn-suma'); // suma
let n = parseInt(count.innerText);

const suma = () => {
    n++;
    count.innerText = n;
};

const resta = () => {
    n--;
    count.innerText = n;
};
// asignar respectivamente la funciones al evento "click"
btnSuma.addEventListener("click", suma);
btnResta.addEventListener("click", resta);