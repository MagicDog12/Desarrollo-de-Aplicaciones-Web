# Ejercicio 2

**Nombre**: Cristian Durán

---

## Pregunta 1
¿Por qué se prefiere enviar un formulario al servidor usando el método POST que el método GET? Investigue. ¿En qué casos se puede usar GET?

**Respuesta**: 

Se prefiere el uso del método POST para enviar un formulario debido a las siguietes razones:
1. Es más seguro que el método GET ya que los datos no se muestran en la URL y por lo tanto no se pueden alterar fácilmente los datos enviados.
2. Este método permite enviar una mayor cantidad de datos.
3. Ayuda a prevenir la repetición accidental de envíos de formularios debido a que utiliza un toke CSRF que garantiza que cada solicitud eviada al servidor sea única y no pueda ser reutilizada.

El método GET es mejor usarlo cuando se quiere solicitar datos y no modificarlos, cuando buscas información en un base de datos o se muestra información estática.

## Pregunta 2
Existen variadas librerías y *frameworks* de Javascript que se pueden utilizar para programar tareas más complejas en el Frontend y manipular el DOM con mayor facilidad. Investigue, nombre y describa 3 de las librerías o Frameworks de javascript más usados en el desarrollo web (por ejemplo, **JQuery**). Si tuviese que implementar su página web ¿Cuál utilizaría?   

**Respuesta**:

Las librerias que más me llamaron la atención al investigar son las siguientes:

1. React: Desarrollado por Facebook, utiliza un enfoque basado en componentes para construir iterfaces de usuario interactivas y reutilizables, usa el DOM virtual que es más rápida y eficiente que la manipulación del DOM real, lo que ayuda a mejorar el rendimiento de la aplicación web.
2. Angular: Desarrollado por Google, es una herramienta potente para construir aplicaciones web complejas y dinámicas. Tiene un enfoque basado en componentes, por lo que permite construir aplicaciones web escalables y fáciles de mantener. 
3. D3.js: Este Framework no lo había escuchado antes pero se ve muy útil, se usa para crear visualizaciones de datos complejas y dinámicas. Utiliza el poder de HTML, CSS, SVG para crear gráficos interactivos y animaciones de datos en tiempo real. Es muy flexible y personalizable. 

Si tuviese que implementar mi página web utilizaría React o Angular ya que se ven muy beneficiosos.