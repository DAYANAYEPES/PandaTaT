from services.db_connection import get_connection
from model.pedidos import Pedido # type: ignore

class PedidosControl:

    @staticmethod
    def obtener_pedidos_por_estado(estado_id: int):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT * FROM Pedidos WHERE estado_id = %s
        """
        cursor.execute(query, (estado_id,))
        results = cursor.fetchall()
        pedidos = [Pedido(**row).to_dict() for row in results]
        cursor.close()
        conn.close()
        return pedidos
