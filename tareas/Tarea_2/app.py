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
@app.route("/informacion-pedido/<int:info>")
def informacion_pedido(info):
    info = int(request.args.get("info", info))
    pedido = None
    c = getConnection()
    pedido = get_pedido(c, info)
    return render_template("informacion-pedido.html", pedido = pedido)

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
            sqlAux = "SELECT nombre, region_id FROM comuna WHERE id = " + str(ped[1]);
            cursor = c.cursor()
            cursor.execute(sqlAux)
            c.commit()
            datos = cursor.fetchall()[0]
            comuna = datos[0]
            region_id = datos[1]
            sqlAux2 = "SELECT nombre FROM region WHERE id = " + str(region_id);
            cursor = c.cursor()
            cursor.execute(sqlAux2)
            c.commit()
            region = cursor.fetchall()[0][0]
            pedidoNew = Pedido(escape(ped[0]), escape(ped[1]), escape(region), escape(comuna), escape(ped[2]), escape(ped[3]), escape(ped[4]), escape(ped[5]), escape(ped[6]), escape(ped[7]))
            listaPedidos.append(pedidoNew)
    return listaPedidos

def get_pedido(c, info):
    sql = "SELECT id, comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante FROM pedido WHERE id =  %s";
    cursor = c.cursor()
    cursor.execute(sql, info)
    c.commit()
    pedido = cursor.fetchall()[0]
    sqlAux = "SELECT nombre, region_id FROM comuna WHERE id = " + str(pedido[1]);
    cursor = c.cursor()
    cursor.execute(sqlAux)
    c.commit()
    datos = cursor.fetchall()[0]
    comuna = datos[0]
    region_id = datos[1]
    sqlAux2 = "SELECT nombre FROM region WHERE id = " + str(region_id);
    cursor = c.cursor()
    cursor.execute(sqlAux2)
    c.commit()
    region = cursor.fetchall()[0][0]
    pedidoNew = Pedido(escape(pedido[0]), escape(pedido[1]), escape(region), escape(comuna), escape(pedido[2]), escape(pedido[3]), escape(pedido[4]), escape(pedido[5]), escape(pedido[6]), escape(pedido[7]))
    return pedidoNew

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