from model  import BaseModel
#aqui tambien hereda de la clase base model 
class Usuario(BaseModel):
    def __init__(self, id, nombre, correo, rol_id):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.rol_id = rol_id
