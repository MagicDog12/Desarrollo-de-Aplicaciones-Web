class Pedido:
    def __init__(self, id, comuna_id, region, comuna, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante):
        self.id = id
        self.comuna_id = comuna_id
        self.region = region
        self.comuna = comuna
        self.tipo = tipo
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.nombre_solicitante = nombre_solicitante
        self.email_solicitante = email_solicitante
        self.celular_solicitante = celular_solicitante

class Donacion:
    def __init__(self, id, comuna_id, region, comuna, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular, ruta):
        self.id = id
        self.comuna_id = comuna_id
        self.region = region
        self.comuna = comuna
        self.calle_numero = calle_numero
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha_disponibilidad = fecha_disponibilidad
        self.descripcion = descripcion
        self.condiciones_retirar = condiciones_retirar
        self.nombre = nombre
        self.email = email
        self.celular = celular
        self.ruta = ruta