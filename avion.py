"""Nuevo producto concreto (actividad 3.5)."""
from transportes import Transporte


class Avion(Transporte):
    def entrega(self) -> str:
        return "Avión: entregando la carga por aire."
