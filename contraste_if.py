"""Actividad 3.8: versión SIN el patrón, con if/elif en el cliente."""
import sys

from avion import Avion
from transportes import Barco, Camion, Transporte


def planificar_entrega(tipo: str) -> str:
    transporte: Transporte
    if tipo == "terrestre":
        transporte = Camion()
    elif tipo == "maritima":
        transporte = Barco()
    elif tipo == "aerea":  # cada transporte nuevo obliga a tocar este código
        transporte = Avion()
    else:
        raise ValueError(f"Tipo desconocido: {tipo}")
    return f"Planificando la ruta de entrega...\n{transporte.entrega()}"


if __name__ == "__main__":
    print(planificar_entrega(sys.argv[1] if len(sys.argv) > 1 else "terrestre"))
