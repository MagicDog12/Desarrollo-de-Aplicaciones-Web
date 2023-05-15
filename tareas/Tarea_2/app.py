from flask import Flask, render_template, request
from markupsafe import escape
from clases import Pedido
import pymysql

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
    error = None
    mensaje = None
    c = getConnection()
    if request.method == 'POST':
        if(agrega_pedido(c, request.form['comuna'], request.form['tipo'], request.form['descripcion'],
                         request.form['cantidad'], request.form['nombre'], request.form['email'], request.form['celular'])):
            mensaje = "Agregado nuevo pedido " + request.form['nombre']
        else:
            error = "No se pudo agregar el pedido"
    return render_template("agregar-pedido.html")

# Definimos una ruta para la URL "/ver-donaciones" y devolvemos el contenido de "ver-donaciones.html"
@app.route("/ver-donaciones")
def ver_donaciones():
    return render_template("ver-donaciones.html")

# Definimos una ruta para la URL "/ver-pedidos" y devolvemos el contenido de "ver-pedidos.html"
@app.route("/ver-pedidos", defaults = {"contador": 0})
@app.route("/ver-pedidos/<int:contador>")
def ver_pedidos(contador):
    contador = int(request.args.get("contador", contador))
    pedidos = None
    c = getConnection()
    pedidos = get_pedidos(c, contador*5)
    return render_template("ver-pedidos.html", pedidos = pedidos, contador = contador)

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

# Se obtiene la conexion con la base de datos
def getConnection():
    conn = pymysql.connect(
        db = 'tarea2',
        user = 'cc5002',
        passwd = 'programacionweb',
        host = 'localhost',
        charset = 'utf8'
    )
    return conn

def get_pedidos(c, contador):
    sql = "SELECT id, comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante FROM pedido ORDER BY id DESC LIMIT %s,5";
    cursor = c.cursor()
    cursor.execute(sql, contador)
    c.commit()
    pedidos = cursor.fetchall()
    listaPedidos = []
    if len(pedidos) > 0:
        for ped in pedidos:
            sqlAux = "SELECT nombre FROM comuna WHERE id = " + str(ped[1]);
            cursor = c.cursor()
            cursor.execute(sqlAux)
            c.commit()
            comuna = cursor.fetchall()[0][0]
            pedidoNew = Pedido(ped[0], ped[1], comuna, ped[2], ped[3], ped[4], ped[5], ped[6], ped[7])
            listaPedidos.append(pedidoNew)
    return listaPedidos

def agrega_pedido(c, comuna, tipo, descripcion, cantidad, nombre, email, celular):
    if not nombre or not tipo:
        return False
    sqlAux = "SELECT id FROM comuna WHERE nombre = %s";
    cursor = c.cursor()
    cursor.execute(sqlAux, comuna)
    c.commit()
    comuna_id = cursor.fetchall()
    sql = "INSERT INTO pedido (comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante) VALUES (%s, %s, %s, %s, %s, %s, %s)";
    try:
        resultado = c.cursor().execute(sql, (comuna_id, tipo, descripcion, cantidad, nombre, email, celular))
        c.commit()
        return resultado == 1
    except pymysql.Error as e:
        app.logger.error("Error con base de datos: {0} {1} ".format(e.args[0], e.args[1]))
        return False

if __name__ == "__main__":
    app.run()