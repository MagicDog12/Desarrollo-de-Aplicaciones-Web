# Tarea 2 de Desarrollo de Aplicaciones Web:

## Consideraciones: 
1. El deployment lo estoy haciendo en un servidor propio, se puede visualizar mi página del curso [Aquí](https://cc5002.cduran.cl/) y el deployment de la tarea 2 [Aquí](https://cc5002.cduran.cl/tareas/Tarea_2/).
2. Se está usando [Bootstrap 5](https://getbootstrap.com/) para facilitar el desarrollo visual de la app.
3. Por lo anterior se redujo al mínimo el contenido de los archivos CSS donde solo se ajustan ciertos detalles.
4. Se utiliza Flask para implementar está aplicación web por lo tanto para instalar el ambiente virtual es necesario ejecutar los siguientes comandos en consola:
```
> py -m venv .venv
> .venv\Scripts\activate
> pip install Flask
> set FLASK_APP=app.py
> flask run
```
5. Para correr la app en [LocalHost, puerto: 5000](http://localhost:5000/) es necesario ejecutar los siguientes comandos en consola:
```
// En Windows:
> .venv\Scripts\activate
// En Linux:
> source .venv/Scripts/activate
> flask run
```