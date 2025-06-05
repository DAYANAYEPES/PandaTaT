from fastapi import FastAPI
from routes import router

app = FastAPI(title="API de PandaPedidos")

app.include_router(router)

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}
