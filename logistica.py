"""Creadora: Logistica. No importa ninguna clase de transporte concreta."""
from abc import ABC, abstractmethod

from transportes import Transporte


class Logistica(ABC):
    @abstractmethod
    def crear_transporte(self) -> Transporte:
        """Método fábrica: las subclases deciden qué transporte devuelven."""
        ...

    def planificar_entrega(self) -> str:
        """Lógica de negocio: usa el transporte sin saber de qué clase es."""
        transporte = self.crear_transporte()
        return f"Planificando la ruta de entrega...\n{transporte.entrega()}"
