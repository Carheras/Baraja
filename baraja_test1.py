import unittest
from unittest.mock import patch
import baraja1

def mi_eligecarta(i, longitud):
    if i == longitud-1:
        return 0
    else:
        return i + 1


class BarajaTest(unittest.TestCase):
    

    def test_crear_baraja(self):
        
        b = baraja1.baraja()
        self.assertEqual(len(b), 40)
        self.assertEqual(b, ['Aso', '2o', '3o', '4o', '5o', '6o', '7o', 'So', 'Co', 'Ro', 'Asc', '2c', '3c', '4c', '5c', '6c', '7c', 'Sc', 'Cc', 'Rc', 'Ase', '2e', '3e', '4e', '5e', '6e', '7e', 'Se', 'Ce', 'Re', 'Asb', '2b', '3b', '4b', '5b', '6b', '7b', 'Sb', 'Cb', 'Rb'])
        self.assertEqual(b[0], "Aso")
        self.assertEqual(b[39], "Rb")
        self.assertEqual(b[10], "Asc")
        self.assertEqual(b[20], "Ase")

    @patch("baraja1.elige_carta", mi_eligecarta)
    def test_mezclar_lista(self):
        x = ["A", "B", "C", "D", "E"] 
        mezclada = ["A", "C", "D", "E", "B"]  
        x = baraja1.mezclar(x)
        self.assertEqual(x, mezclada)


if __name__ == "__main__":
    unittest.main()
    

