from .base import ModeloBase
#aquii herada de la clase principla los atributos que muetsfan los pedidos 
class Pedido(ModeloBase):
    def __init__(self, id, descripcion, usuario_id, estado_id, fecha):
        self.id = id
        self.descripcion = descripcion
        self.usuario_id = usuario_id
        self.estado_id = estado_id
        self.fecha = fecha