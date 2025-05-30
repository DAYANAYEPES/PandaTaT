from fastapi import FastAPI
from routers import app 


app = FastAPI(title="API de PandaPedidos")


@app.get("/prueba")
def inicio():
    return {"mensaje": "API funcionando correctamente"}

