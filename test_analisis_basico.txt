"""Evidencia reproducible de los requisitos de la práctica."""
import contextlib
import inspect
import io
import unittest
import analisis_basico as practica


class TestPractica(unittest.TestCase):
    def test_tipos_basicos(self):
        self.assertIsInstance(practica.producto, str)
        self.assertIsInstance(practica.precio, float)
        self.assertIs(type(practica.stock), int)
        self.assertIs(type(practica.tiene_descuento), bool)

    def test_lista_y_diccionario(self):
        self.assertIsInstance(practica.precios, list)
        self.assertGreaterEqual(len(practica.precios), 5)
        self.assertTrue(all(type(x) in (int, float) for x in practica.precios))
        self.assertEqual(practica.almacen['Auriculares'], 15)
        self.assertEqual(practica.almacen['Mouse'], 25)

    def test_firma_un_solo_parametro(self):
        self.assertEqual(list(inspect.signature(practica.resumen_estadistico).parameters), ['numeros'])

    def test_resumen_ejemplo_consigna(self):
        self.assertEqual(practica.resumen_estadistico([10, 20, 30]),
                         {'total': 60, 'promedio': 20.0, 'cantidad': 3})

    def test_resumen_decimales_y_negativos(self):
        self.assertEqual(practica.resumen_estadistico([-2.5, 0, 4]),
                         {'total': 1.5, 'promedio': 0.5, 'cantidad': 3})

    def test_lista_vacia(self):
        self.assertEqual(practica.resumen_estadistico([]),
                         {'total': 0, 'promedio': None, 'cantidad': 0})

    def test_no_modifica_entrada(self):
        numeros = [30, 10, 20]
        practica.resumen_estadistico(numeros)
        self.assertEqual(numeros, [30, 10, 20])

    def test_salida_y_umbral(self):
        captura = io.StringIO()
        with contextlib.redirect_stdout(captura):
            practica.main()
        salida = captura.getvalue()
        self.assertIn('$100.00: Económico', salida)
        self.assertIn('$125.50: Caro', salida)
        self.assertIn('Stock de Mouse: 25', salida)
        self.assertIn('Producto: Teclado; precio: $125.50', salida)
        self.assertIn("'total': 560.5", salida)


if __name__ == '__main__':
    unittest.main(verbosity=2)
