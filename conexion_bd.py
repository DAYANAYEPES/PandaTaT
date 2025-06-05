import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3308,
        user="root",
        password="",
        database="pandatat"
    )
