from flask import Flask, render_template
# Creamos una instancia de Flask en el módulo actual
app = Flask(__name__)


# Definimos una ruta para la URL principal y devolvemos el contenido de 'inicio.html'
@app.route("/")
def inicio():
    return render_template("inicio.html")

# Verificamos si la aplicación Flask se está ejecutando directamente desde el archivo 'app.py'
# y para ejecutar el servidor Flask en el puerto especificado (:5000)
if __name__ == "__main__":
    app.run()