import unittest

from avion import Avion
from logistica import Logistica
from logistica_aerea import LogisticaAerea
from logistica_maritima import LogisticaMaritima
from logistica_terrestre import LogisticaTerrestre
from transportes import Barco, Camion, Transporte

CREADORES = [LogisticaTerrestre, LogisticaMaritima, LogisticaAerea]


class PruebasFactoryMethod(unittest.TestCase):
    def test_cada_creador_devuelve_su_producto(self) -> None:
        self.assertIsInstance(LogisticaTerrestre().crear_transporte(), Camion)
        self.assertIsInstance(LogisticaMaritima().crear_transporte(), Barco)
        self.assertIsInstance(LogisticaAerea().crear_transporte(), Avion)

    def test_productos_cumplen_la_interfaz(self) -> None:
        for clase in (Camion, Barco, Avion):
            self.assertTrue(issubclass(clase, Transporte))
            self.assertIsInstance(clase().entrega(), str)

    def test_planificar_entrega_funciona_con_cualquier_creador(self) -> None:
        for clase in CREADORES:
            logistica: Logistica = clase()  # se usa solo como Logistica
            texto = logistica.planificar_entrega()
            self.assertIn("Planificando la ruta", texto)
            self.assertIn("entregando la carga", texto)

    def test_reutilizacion_devuelve_la_misma_instancia(self) -> None:
        logistica = LogisticaMaritima()
        self.assertIs(logistica.crear_transporte(), logistica.crear_transporte())

    def test_no_se_pueden_instanciar_las_clases_abstractas(self) -> None:
        with self.assertRaises(TypeError):
            Transporte()  # type: ignore[abstract]
        with self.assertRaises(TypeError):
            Logistica()  # type: ignore[abstract]


if __name__ == "__main__":
    unittest.main()
