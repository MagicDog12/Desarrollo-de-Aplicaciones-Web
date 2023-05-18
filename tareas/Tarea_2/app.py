import os
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
from clases import Pedido, Donacion
import pymysql
from werkzeug.utils import secure_filename
import re
from datetime import datetime

# Asignamos la carpeta donde se almacenan los archivos
UPLOAD_FOLDER = 'static/img/'
ALLOWED_EXTENSIONS = {'img', 'png', 'jpg', 'jpeg'}

# Creamos una instancia de Flask en el módulo actual
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

# Definimos una ruta para la URL principal y devolvemos el contenido de 'inicio.html'
@app.route("/")
def inicio():
    return render_template("inicio.html")
    
# Definimos una ruta para la URL "/agregar-donacion" y devolvemos el contenido de "agregar-donacion.html"
@app.route("/agregar-donacion", methods=['GET', 'POST'])
def agregar_donacion():
    error = None
    mensaje = None
    c = getConnection()
    if request.method == 'POST':
        # revisa si el post request tiene un archivo
        if 'foto-1' not in request.files:
            error = "No hay ninguna foto"
            return render_template("agregar-donacion.html", error = error)
        
        foto1 = request.files['foto-1']
        foto2 = False
        foto3 = False
        if 'foto-2' in request.files:
            foto2 = request.files['foto-2']
        if 'foto-3' in request.files:
            foto3 = request.files['foto-3']
        filename = ''
        filename2 = ''
        filename3 = ''
        if foto1.filename == '':
            error = "Ninguna foto seleccionada"
            return render_template("agregar-donacion.html", error = error)
        
        if foto1 and allowed_file(foto1.filename):
            filename = secure_filename(foto1.filename)
            foto1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        if foto2 and allowed_file(foto2.filename):
            filename2 = secure_filename(foto2.filename)
            foto2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))

        if foto3 and allowed_file(foto3.filename):
            filename3 = secure_filename(foto3.filename)
            foto3.save(os.path.join(app.config['UPLOAD_FOLDER'], filename3))

        if(agrega_donacion(c, request.form['comuna'], request.form['calle-numero'], request.form['tipo'], request.form['cantidad'],
                         request.form['fecha-disponibilidad'], request.form['descripcion'], request.form['condiciones'], 
                         filename, filename2, filename3, request.form['nombre'], request.form['email'], request.form['celular'])):
            mensaje = "Agregado correctamente "
        else:
            error = "No se pudo agregar la donacion"
    return render_template("agregar-donacion.html", error = error)

# Definimos una ruta para la URL "/agregar-pedido" y devolvemos el contenido de "agregar-pedido.html"
@app.route("/agregar-pedido", methods=['GET', 'POST'])
def agregar_pedido():
    error = None
    mensaje = None
    c = getConnection()
    if request.method == 'POST':
        if(agrega_pedido(c, request.form['comuna'], request.form['tipo'], request.form['descripcion'],
                         request.form['cantidad'], request.form['nombre'], request.form['email'], request.form['celular'])):
            mensaje = "Agregado correctamente "
        else:
            error = "No se pudo agregar el pedido"
    return render_template("agregar-pedido.html", error = error)

# Definimos una ruta para la URL "/ver-donaciones" y devolvemos el contenido de "ver-donaciones.html"
@app.route("/ver-donaciones", defaults = {"contador": 0})
@app.route("/ver-donaciones/<int:contador>")
def ver_donaciones(contador):
    contador = int(request.args.get("contador", contador))
    donaciones = None
    c = getConnection()
    donaciones = get_donaciones(c, contador*5)
    return render_template("ver-donaciones.html", donaciones = donaciones, contador = contador)

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
@app.route("/informacion-donacion/<int:info>")
def informacion_donacion(info):
    info = int(request.args.get("info", info))
    donacion = None
    c = getConnection()
    donacion = get_donacion(c, info)
    return render_template("informacion-donacion.html", donacion = donacion)

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

def get_donaciones(c, contador):
    sql = "SELECT id, comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular FROM donacion ORDER BY id DESC LIMIT %s,5";
    cursor = c.cursor()
    cursor.execute(sql, contador)
    c.commit()
    donaciones = cursor.fetchall()
    listaDonaciones = []
    if len(donaciones) > 0:
        for don in donaciones:
            sqlAux = "SELECT nombre, region_id FROM comuna WHERE id = " + str(don[1]);
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
            # rutas
            rutas = []
            sql_ruta = "SELECT ruta_archivo FROM foto WHERE donacion_id = " + str(don[0]);
            cursor = c.cursor()
            cursor.execute(sql_ruta)
            c.commit()
            rutasAntes = cursor.fetchall()
            for ruta in rutasAntes:
                rutas.append(ruta[0].replace("static/", ""))

            fechaAntes = escape(don[5])
            fecha = fechaAntes[:10]
            donacionNew = Donacion(escape(don[0]), escape(don[1]), escape(region), escape(comuna), escape(don[2]), escape(don[3]), escape(don[4]), fecha, escape(don[6]), escape(don[7]), escape(don[8]), escape(don[9]), escape(don[10]), rutas)
            listaDonaciones.append(donacionNew)
    return listaDonaciones


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

def get_donacion(c, info):
    sql = "SELECT id, comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular FROM donacion WHERE id =  %s";
    cursor = c.cursor()
    cursor.execute(sql, info)
    c.commit()
    don = cursor.fetchall()[0]
    sqlAux = "SELECT nombre, region_id FROM comuna WHERE id = " + str(don[1]);
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
    # rutas
    rutas = []
    sql_ruta = "SELECT ruta_archivo FROM foto WHERE donacion_id = " + str(don[0]);
    cursor = c.cursor()
    cursor.execute(sql_ruta)
    c.commit()
    rutasAntes = cursor.fetchall()
    for ruta in rutasAntes:
        rutas.append(ruta[0].replace("static/", ""))

    fechaAntes = escape(don[5])
    fecha = fechaAntes[:10]
    donacionNew = Donacion(escape(don[0]), escape(don[1]), escape(region), escape(comuna), escape(don[2]), escape(don[3]), escape(don[4]), fecha, escape(don[6]), escape(don[7]), escape(don[8]), escape(don[9]), escape(don[10]), rutas)
    return donacionNew

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

def agrega_donacion(c, comuna, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones, foto1, foto2, foto3, nombre, email, celular):
    if validacion_donacion(comuna, calle_numero, tipo, cantidad, fecha_disponibilidad, nombre, email, celular):
        return False
    sqlAux = "SELECT id FROM comuna WHERE nombre = %s";
    cursor = c.cursor()
    cursor.execute(sqlAux, comuna)
    c.commit()
    comuna_id = cursor.fetchall()
    sql = "INSERT INTO donacion (comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)";
    slqFoto = "INSERT INTO foto (ruta_archivo, nombre_archivo, donacion_id) VALUES (%s, %s, %s)";
    try:
        cursor = c.cursor()
        resultado = cursor.execute(sql, (comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones, nombre, email, celular))
        c.commit()
        id_foto = cursor.lastrowid
        ruta1 = os.path.join(app.config['UPLOAD_FOLDER'], foto1)
        resultadoFoto1 = cursor.execute(slqFoto, (ruta1,  foto1, id_foto))
        c.commit()
        resultadoFoto2 = 1
        if(foto2 != ''):
            ruta2 = os.path.join(app.config['UPLOAD_FOLDER'], foto2)
            resultadoFoto2 = cursor.execute(slqFoto, (ruta2,  foto2, id_foto))
            c.commit()
        resultadoFoto3 = 1
        if(foto3 != ''):
            ruta3 = os.path.join(app.config['UPLOAD_FOLDER'], foto3)
            resultadoFoto3 = cursor.execute(slqFoto, (ruta3,  foto3, id_foto))
            c.commit()
        return resultado == 1 and resultadoFoto1 == 1 and resultadoFoto2 == 1 and resultadoFoto3 == 1
    except pymysql.Error as e:
        app.logger.error("Error con base de datos: {0} {1} ".format(e.args[0], e.args[1]))
        return False

def agrega_pedido(c, comuna, tipo, descripcion, cantidad, nombre, email, celular):
    if validacion_pedido(comuna, tipo, descripcion, cantidad, nombre, email, celular):
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

# si retorna true es porque no pasa la validacion
def validacion_donacion(comuna, calle_numero, tipo, cantidad, fecha_disponibilidad, nombre, email, celular):
    if not comuna or not tipo or not calle_numero or not cantidad:
        return True
    if len(nombre) < 3 or len(nombre) > 250:
        return True
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    if not re.match(r"^9\d{8}$", celular) and celular:
        return True
    try:
        fecha_actual = datetime.now().date()
        fecha_donacion = datetime.strptime(fecha_disponibilidad, "%Y-%m-%d").date()
        
        if fecha_donacion < fecha_actual:
            return True
    except ValueError:
        return True
    return False

# si retorna true es porque no pasa la validacion
def validacion_pedido(comuna, tipo, descripcion, cantidad, nombre, email, celular):
    if not comuna or not tipo:
        return True
    if not descripcion or len(descripcion) > 250:
        return True
    if not cantidad:
        return True
    if len(nombre) < 3 or len(nombre) > 250:
        return True
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    if not re.match(r"^9\d{8}$", celular) and celular:
        return True
    return False

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)