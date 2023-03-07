from ast import main
import sys

numero_magico=12345679

def numeromagico():
    numeroint=int(input("Introduzca un numero del 0 al 9: "))
    if 0<=numeroint<=9:

        print(numeroint) 
    else:
        print("valor no aceptado", file=sys.stderr)
        numeromagico()

    print("Has introducido el numero: ", numeroint)
    print("El numero magico es: ", numero_magico)
    print("Al multiplicar el numero introducido por 9, el resultado es: ", numeroint*9)
    print("Al multiplicar el numero magico por el resultado anterior, el resultado es: ", numero_magico*(numeroint*9))

print(numeromagico())

        



if __name__=="__main__":
    main()