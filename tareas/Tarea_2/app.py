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
    return render_template("agregar-pedido.html")

@app.route("/ver-donaciones")
def ver_donaciones():
    return render_template("ver-donaciones.html")

@app.route("/ver-pedidos")
def ver_pedidos():
    return render_template("ver-pedidos.html")

@app.route("/informacion-donacion")
def informacion_donacion():
    return render_template("informacion-donacion.html")

@app.route("/informacion-pedido")
def informacion_pedido():
    return render_template("informacion-pedido.html")

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