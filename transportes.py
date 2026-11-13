"""Producto (interfaz Transporte) y productos concretos Camion y Barco."""
from abc import ABC, abstractmethod


class Transporte(ABC):
    """Interfaz común: todos los transportes tienen que saber hacer entrega()."""

    @abstractmethod
    def entrega(self) -> str:
        ...


class Camion(Transporte):
    def entrega(self) -> str:
        return "Camión: entregando la carga por tierra."


class Barco(Transporte):
    def entrega(self) -> str:
        return "Barco: entregando la carga por mar."
