from fastapi import APIRouter
from gestionPedidos import GestionPedidos

router = APIRouter()

@router.get("/pedidos/enviados")
def pedidos_enviados():
    return GestionPedidos.obtener_por_estado(1)

@router.get("/pedidos/cancelados")
def pedidos_cancelados():
    return GestionPedidos.obtener_por_estado(2)

@router.get("/pedidos/pagados")
def pedidos_pagados():
    return GestionPedidos.obtener_por_estado(3)

@router.get("/pedidos/reenviados")
def pedidos_reenviados():
    return GestionPedidos.obtener_por_estado(4)
