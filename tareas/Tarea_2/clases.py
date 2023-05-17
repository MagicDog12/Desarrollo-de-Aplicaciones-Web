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