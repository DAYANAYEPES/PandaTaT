from fastapi import APIRouter
from controllers.pedidosControl import PedidosControl

router = APIRouter()

@router.get("/pedidos/enviados")
def get_pedidos_enviados():
    return PedidosControl.obtener_pedidos_por_estado(1)

@router.get("/pedidos/cancelados")
def get_pedidos_cancelados():
    return PedidosControl.obtener_pedidos_por_estado(2)

@router.get("/pedidos/pagados")
def get_pedidos_pagados():
    return PedidosControl.obtener_pedidos_por_estado(3)

@router.get("/pedidos/reenviados")
def get_pedidos_reenviados():
    return PedidosControl.obtener_pedidos_por_estado(4)

