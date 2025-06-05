from modelos.base import ModeloBase

class Pedidos:
    def __init__(self, id, descripcion, usuario_id, estado_id, fecha):
        self.id = id
        self.descripcion = descripcion
        self.usuario_id = usuario_id
        self.estado_id = estado_id
        self.fecha = fecha

    def to_dict(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "usuario_id": self.usuario_id,
            "estado_id": self.estado_id,
            "fecha": self.fecha
        }