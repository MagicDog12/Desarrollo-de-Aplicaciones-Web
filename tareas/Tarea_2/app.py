from flask import Flask, render_template, request
from markupsafe import escape

# Creamos una instancia de Flask en el módulo actual
app = Flask(__name__)

# Definimos una ruta para la URL principal y devolvemos el contenido de 'inicio.html'
@app.route("/")
def inicio():
    return render_template("inicio.html")
    
# Definimos una ruta para la URL "/agregar-donacion" y devolvemos el contenido de "agregar-donacion.html"
@app.route("/agregar-donacion", methods=['GET', 'POST'])
def agregar_donacion():
    return render_template("agregar-donacion.html")

# Definimos una ruta para la URL "/agregar-pedido" y devolvemos el contenido de "agregar-pedido.html"
@app.route("/agregar-pedido", methods=['GET', 'POST'])
def agregar_pedido():
    return render_template("agregar-pedido.html")

# Definimos una ruta para la URL "/ver-donaciones" y devolvemos el contenido de "ver-donaciones.html"
@app.route("/ver-donaciones")
def ver_donaciones():
    return render_template("ver-donaciones.html")

# Definimos una ruta para la URL "/ver-pedidos" y devolvemos el contenido de "ver-pedidos.html"
@app.route("/ver-pedidos")
def ver_pedidos():
    return render_template("ver-pedidos.html")

# Definimos una ruta para la URL "/informacion-donacion" y devolvemos el contenido de "informacion-donacion.html"
@app.route("/informacion-donacion")
def informacion_donacion():
    return render_template("informacion-donacion.html")

# Definimos una ruta para la URL "/informacion-pedido" y devolvemos el contenido de "informacion-pedido.html"
@app.route("/informacion-pedido")
def informacion_pedido():
    return render_template("informacion-pedido.html")

# Definir la función de manejo de errores 404
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html'), 404


# @app.route('/login', methods=['GET', 'POST'])
# def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Aquí puedes autenticar al usuario
        return f'¡Hola, {escape(username)}! Tu contraseña es: {escape(password)}'
    else:
        return '''
        <form method="post">
            <label>Nombre de usuario:</label>
            <input type="text" name="username"><br>
            <label>Contraseña:</label>
            <input type="password" name="password"><br>
            <input type="submit" value="Iniciar sesión">
        </form>
        '''

if __name__ == "__main__":
    app.run()