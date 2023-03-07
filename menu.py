import helpers
import os
from EJERCICIOS import ejercicio1
from EJERCICIOS import ejercicio2
from EJERCICIOS import ejercicio3
from EJERCICIOS import ejercicio4
from EJERCICIOS import ejercicio5
from EJERCICIOS import ejercicio6
from EJERCICIOS import ejercicio7

def menu():
    helpers.limpiar_pantalla()
    print("BIENVENIDO AL MENÚ DE EJERCICIOS DEL PARCIAL")
    print("============================================")
    print("    ELIJA EL EJERCICIO QUE DESEA REALIZAR   ")
    print("============================================")
    print("             1. EJERCICIO 1                 ")
    print("             2. EJERCICIO 2                 ")
    print("             3. EJERCICIO 3                 ")
    print("             4. EJERCICIO 4                 ")
    print("             5. EJERCICIO 5                 ")
    print("             6. EJERCICIO 6                 ")
    print("             7. EJERCICIO 7                 ")
    print("             8. SALIR                       ")
    print("============================================")
    opcion = input("Ingrese la opción que desea: ")
    if opcion == "1":
        ejercicio1.ejercicio1()
    elif opcion == "2":
        ejercicio2.ejercicio2()
    elif opcion == "3":
        ejercicio3.ejercicio3()
    elif opcion == "4":
        ejercicio4.ejercicio4()
    elif opcion == "5":
        ejercicio5.ejercicio5()
    elif opcion == "6":
        ejercicio6.ejercicio6()
    elif opcion == "7":
        ejercicio7.ejercicio7()
    elif opcion == "8":
        helpers.limpiar_pantalla()
        print("Gracias por utilizar el programa")
        os._exit(0)