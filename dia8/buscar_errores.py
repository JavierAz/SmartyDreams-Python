"""
Este codigo busca errores con pylint:
 para buscar errores:# pylint archivo... -r y
"""
import unittest
from Paquete_Jav import suma_resta


def fun():
    num = 500
    print(num)


fun()


class Pruebas(unittest.TestCase):
    def test_suma(self):
        suma = [1, 2, 3, 4]
        resultad0 = suma_resta.suma(suma)
        self.assertEqual(resultad0, 10)


if __name__ == '__main__':
    unittest.main()
