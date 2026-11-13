"""Cliente: elige el creador según la configuración y lo usa vía Logistica."""
import sys

from logistica import Logistica
from logistica_aerea import LogisticaAerea
from logistica_maritima import LogisticaMaritima
from logistica_terrestre import LogisticaTerrestre

# Configuración: qué tipo de logística usar si no se pasa argumento.
CONFIG = {"tipo": "terrestre"}

CREADORES: dict[str, type[Logistica]] = {
    "terrestre": LogisticaTerrestre,
    "maritima": LogisticaMaritima,
    "aerea": LogisticaAerea,  # <- única línea de configuración añadida en 3.5
}


def codigo_cliente(logistica: Logistica) -> None:
    """Solo conoce la interfaz base Logistica."""
    print(logistica.planificar_entrega())


def main() -> None:
    tipo = sys.argv[1] if len(sys.argv) > 1 else CONFIG["tipo"]
    if tipo not in CREADORES:
        raise SystemExit(f"Tipo desconocido: {tipo}. Opciones: {', '.join(CREADORES)}")
    codigo_cliente(CREADORES[tipo]())


if __name__ == "__main__":
    main()
