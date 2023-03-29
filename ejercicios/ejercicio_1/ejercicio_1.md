# Ejercicio 1

**Nombre**: Cristian Durán

---

## Pregunta 1
Explique por qué el realizar validaciones del input del usuario en el front-end es una facilidad pero no una medida de seguridad. 

**Respuesta**: Es una facilidad porque permite que el usuario entienda mejor los parametros y restricciones del input, lo que mejora la experiencia de usuario. Y no es una medidad de seguridad ya que estas validaciones estan del lado del cliente por lo que es fácil manipularlas y enviar datos sin restricciones.

## Pregunta 2
Usted cuenta con el siguiente codigo HTML:
```html
<div>
    <p>Contador: <span id="contador">0</span></p>
    <button type="button" id="btn-resta">-1</button>
    <button type="button" id="btn-suma">+1</button>
</div>
```
Implemente un contador bidireccional utilizando la plantilla disponible mas abajo, solo programe donde se le indica. Se espera que tras apretar un boton, el contador se actualice sin la necesidad de recargar la pagina. **No esta permitido modificar el HTML**.

**Respuesta**:
```js
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
```

## Pregunta 3

Explique brevemente qué es el HTML semántico. ¿Qué ventajas tiene? De dos ejemplos de etiquetas (*tags*) semánticas.

**Respuesta**: HTML es un lenguaje de etiquetado por lo que sirve para describir el contenido de la página web, tiene vetajas como hacer más fácil el entendimiento de lo que se quiere mostrar y ayuda a jerarquizar los datos que se quiere visualizar. Dos ejemplos de tags son: "aside" y "section"