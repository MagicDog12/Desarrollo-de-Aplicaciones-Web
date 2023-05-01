from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")
    
@app.route("/agregar-donacion", methods=['GET', 'POST'])
def agregar_donacion():
    return render_template("agregar-donacion.html")

@app.route("/agregar-pedido", methods=['GET', 'POST'])
def agregar_pedido():
    return "<h1> Agregar-pedido.html </h1>"

@app.route("/ver-donaciones")
def ver_donaciones():
    return "<h1> Ver-donaciones.html </h1>"

@app.route("/ver-pedidos")
def ver_pedidos():
    return "<h1> Ver-pedidos.html </h1>"

@app.route("/informacion-donacion")
def informacion_donacion():
    return "<h1> Informacion-donacion.html </h1>"

@app.route("/informacion-pedido")
def informacion_pedido():
    return "<h1> Informacion-pedido.html </h1>"

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