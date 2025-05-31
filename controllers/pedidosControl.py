from fastapi import APIRouter
from services.pedidosservice import PedidosService  

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.get("/enviados")
def get_pedidos_enviados():
    return PedidosService.obtener_pedidos_por_estado(1)

@router.get("/cancelados")
def get_pedidos_cancelados():
    return PedidosService.obtener_pedidos_por_estado(2)

@router.get("/pagados")
def get_pedidos_pagados():
    return PedidosService.obtener_pedidos_por_estado(3)

@router.get("/reenviados")
def get_pedidos_reenviados():
    return PedidosService.obtener_pedidos_por_estado(4)
