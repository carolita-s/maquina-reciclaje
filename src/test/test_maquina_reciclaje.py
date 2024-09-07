import unittest
from src.main.maquina_reciclaje import MaquinaReciclajeMetales

class TestMaquinaReciclajeMetales(unittest.TestCase):
    def setUp(self):
        self.maquina = MaquinaReciclajeMetales("Recicladora 3000", 500)

    def test_clasificar_metales(self):
        self.assertEqual(self.maquina.clasificar_metales("hierro"), "Hierro")
        self.assertEqual(self.maquina.clasificar_metales("aluminio"), "Aluminio")
        self.assertEqual(self.maquina.clasificar_metales("plástico"), "Otro")

    def test_compactar_metales(self):
        self.assertEqual(self.maquina.compactar_metales("Hierro"), "Compactando hierro")
        self.assertEqual(self.maquina.compactar_metales("Aluminio"), "Compactando aluminio")

    def test_calcular_eficiencia(self):
        self.assertEqual(self.maquina.calcular_eficiencia(1000, 2), "Eficiencia: 500.0 kg/h")

if __name__ == '__main__':
    unittest.main()
    