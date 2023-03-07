from ast import main
import sys

class Ej5:
    def num():
        while True:
            numeros=input("Valor: ")
            try:
                numeros=int(numeros)
            except:
                print("valor no aceptado", file=sys.stderr)
            else:
                break
        return str(numeros)

    def descomponer():
        numeros=Ej5.num()
        numero=numeros[::-1]
        ceros_izquierda=0
        while True:
            for i in str(numero):
                ceros_izquierda+=1
                print((i.ljust(int(ceros_izquierda),'0')).zfill(len(numero)), "\n")
            if ceros_izquierda >= len(numero):
                break



if __name__=="__main__":
    print(Ej5.descomponer())