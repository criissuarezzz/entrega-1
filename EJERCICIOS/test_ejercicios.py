import copy
import unittest
import config
import ejercicio1
import ejercicio2

class TestEjercicios(unittest.TestCase):
    def test_alumno(self):
        nombre=ejercicio1.Alumno("zeréP nauJ,01")
        self.assertEqual(ejercicio1.Alumno.transformar_cadena(nombre.cadena), "Juan Pérez ha sacado un 10")

    def test_numero_magico(self):
        numero=ejercicio2.num()
        self.assertEqual(ejercicio2.numero_magico())

    

        
        