
import unittest
from unittest.mock import patch
from src.views.filtro_vehiculos import mostrar_filtro


class TestGC0352(unittest.TestCase):

    def setUp(self):
        self.vehiculos = [
            {
                "id_vehiculo": "VEH-01",
                "modelo": "Toyota Yaris",
                "tipo": "COCHE",
                "disponible": True
            },
            {
                "id_vehiculo": "VEH-02",
                "modelo": "Ford Transit",
                "tipo": "FURGONETA",
                "disponible": True
            },
            {
                "id_vehiculo": "VEH-03",
                "modelo": "Peugeot 208",
                "tipo": "COCHE",
                "disponible": False
            }
        ]

    def filtrar_simulado(self, tipo):
        if tipo == "TODOS":
            return self.vehiculos
        return [
            v for v in self.vehiculos
            if v["tipo"] == tipo
        ]

    def test_seleccionar_coche(self):
        with patch(
            "src.views.filtro_vehiculos.filtrar_por_tipo",
            side_effect=self.filtrar_simulado
        ):
            resultado = mostrar_filtro("COCHE")

        self.assertIn("Toyota Yaris", resultado)
        self.assertNotIn("Ford Transit", resultado)

    def test_seleccionar_furgoneta(self):
        with patch(
            "src.views.filtro_vehiculos.filtrar_por_tipo",
            side_effect=self.filtrar_simulado
        ):
            resultado = mostrar_filtro("FURGONETA")

        self.assertIn("Ford Transit", resultado)
        self.assertNotIn("Toyota Yaris", resultado)

    def test_solo_vehiculos_disponibles(self):
        with patch(
            "src.views.filtro_vehiculos.filtrar_por_tipo",
            side_effect=self.filtrar_simulado
        ):
            resultado = mostrar_filtro("TODOS")

        self.assertNotIn("Peugeot 208", resultado)

    def test_eliminar_filtro(self):
        with patch(
            "src.views.filtro_vehiculos.filtrar_por_tipo",
            side_effect=self.filtrar_simulado
        ):
            resultado = mostrar_filtro("TODOS")

        self.assertIn("Toyota Yaris", resultado)
        self.assertIn("Ford Transit", resultado)

    def test_tipo_sin_resultados(self):
        with patch(
            "src.views.filtro_vehiculos.filtrar_por_tipo",
            return_value=[]
        ):
            resultado = mostrar_filtro("FURGONETA")

        self.assertEqual(
            resultado,
            "No hay resultados para el filtro FURGONETA."
        )


if __name__ == "__main__":
    unittest.main()
