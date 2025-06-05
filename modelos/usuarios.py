# modelos/usuario.py
from modelos.base import ModeloBase

class Usuario(ModeloBase):
    def __init__(self, id, nombre, correo, rol_id):
        self.id = id
        
        self.nombre = str(nombre).strip() 
        self.correo = str(correo).strip() 
        self.rol_id = rol_id