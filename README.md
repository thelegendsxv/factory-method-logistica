# Gestión logística con Factory Method (Python)

Requiere Python 3.10 o superior. No necesita instalar nada.

## Ejecutar
    python main.py              # usa la configuración por defecto (terrestre)
    python main.py maritima     # logística marítima
    python main.py aerea        # logística aérea
    python contraste_if.py aerea   # versión sin patrón (actividad 3.8)

## Pruebas
    python -m unittest -v

## Archivos
- transportes.py: interfaz Transporte, Camion y Barco
- logistica.py: creadora abstracta Logistica (método fábrica + planificar_entrega)
- logistica_terrestre.py / logistica_maritima.py: creadores concretos
- avion.py / logistica_aerea.py: extensión (actividad 3.5)
- main.py: cliente
