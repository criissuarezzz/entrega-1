import copy
import unittest
import config
from EJERCICIOS import ejercicio1

class TestDatabase(unittest.TestCase):
    def testalumno(self):
        nombre=ejercicio1.Alumno("zeréP nauJ,01")
        self.assertEqual(ejercicio1.Alumno.transformar_cadena(nombre.cadena), "Juan Pérez ha sacado un 01")
        