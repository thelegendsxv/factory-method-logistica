"""Nuevo creador concreto (actividad 3.5)."""
from avion import Avion
from logistica import Logistica
from transportes import Transporte


class LogisticaAerea(Logistica):
    def crear_transporte(self) -> Transporte:
        return Avion()
