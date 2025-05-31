#aqui importamos la coneccioon a la base de datos con el mysqlconnector 
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="http://127.0.0.1:8000/",
        user="root",
        password="root",
        database="pandatat"
    )
