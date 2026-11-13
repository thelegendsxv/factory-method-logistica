"""Creador concreto: devuelve camiones."""
from logistica import Logistica
from transportes import Camion, Transporte


class LogisticaTerrestre(Logistica):
    def crear_transporte(self) -> Transporte:
        return Camion()
