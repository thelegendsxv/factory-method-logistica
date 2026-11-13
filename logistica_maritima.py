"""Creador concreto: devuelve barcos y reutiliza el que ya creó (actividad 3.6)."""
from logistica import Logistica
from transportes import Barco, Transporte


class LogisticaMaritima(Logistica):
    def __init__(self) -> None:
        # Mini caché: aquí guardamos el barco una vez creado.
        self._barco: Barco | None = None

    def crear_transporte(self) -> Transporte:
        if self._barco is None:  # solo se hace new la primera vez
            self._barco = Barco()
        return self._barco
