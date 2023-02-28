from ast import main
import sys

numero_magico=12345679

def excepcion():
    while True:
        numero=(input("Nº entre 1 y 9: "))
        try:
            numero=int(numero)
            if 1<=int(numero)<=9:
                return numero
                break
                sys.exit()
            else:
                pass
        except:
            raise ValueError("El caracter ni válido", file=sys.stderr)

def num():
    numero=excepcion()
    n1=numero*9
    print("{} multiplicado por 9 es {}".format(numero, n1))
    valor_magico=numero_magico*n1
    return "{} multiplicado por {} es {}".format(n1, numero_magico, valor_magico)

print(num())
