import copy
import unittest
import config
import ejercicio1

import ejercicio3
import ejercicio4
import ejercicio5
import ejercicio6
import ejercicio7

class TestEjercicios(unittest.TestCase):
    def test_alumno(self):
        nombre=ejercicio1.Alumno("zeréP nauJ,01")
        self.assertEqual(ejercicio1.Alumno.transformar_cadena(nombre.cadena), "Juan Pérez ha sacado un 10")
    
    def test_listas(self):
        lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
        lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
        self.assertEqual(ejercicio3.lista(lista_1, lista_2), ['h', 'o', 'l', 'a', ' ', 'u', 'n'])
    

    def test_prioridad(self):
        ordenar = [
            {'tarea 3': 'ir a clase', 'prioridad':'3'},
            {'tarea 1': 'levantarme', 'prioridad':'1'},
            {'tarea 2': 'comer', 'prioridad':'2'}
        ]
        self.assertEqual(ejercicio4.ordenar(ordenar), [{'tarea 1': 'levantarme', 'prioridad': '1'}, {'tarea 2': 'comer', 'prioridad': '2'}, {'tarea 3': 'ir a clase', 'prioridad': '3'}])

    
    
    
    def test_paresimpares(self):
        self.assertEqual(ejercicio6.separar(1,2,3,4,5,6,7,8,9,10), ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9]))
    
    def test_agregar_una_vez(self):
        self.assertEqual(ejercicio7.agregar_una_vez([1, "Hola", 4, "Adiós"], 6), [1, "Hola", 4, "Adiós", 6])
        self.assertRaises(ValueError, ejercicio7.agregar_una_vez, [1, "Hola", 4, "Adiós"], 4)
     

        
        