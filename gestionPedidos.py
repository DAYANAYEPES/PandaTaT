from conexion_bd import obtener_conexion
from modelos.pedidos import Pedidos

class GestionPedidos:

    @staticmethod
    def obtener_por_estado(estado_id: int):
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Pedidos WHERE estado_id = %s", (estado_id,))
        resultados = cursor.fetchall()
        pedidos = [Pedidos(**row).to_dict() for row in resultados]
        cursor.close()
        conn.close()
        return pedidos
