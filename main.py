from fastapi import FastAPI
from controllers.pedidosControl import router as pedidos_router

app = FastAPI(title="API de PandaPedidos")

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}


app.include_router(pedidos_router)




  