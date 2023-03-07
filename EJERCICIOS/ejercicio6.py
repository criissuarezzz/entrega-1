

def separar(*args):
    lista=[]
    for i in range(1,11):
        valor=int(input("Valor: "))
        lista.append(valor)
    print("La lista resultante es:", lista)

    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0 and i not in pares:
            pares.append(i)
        else:
            impares.append(i)
    pares=sorted(pares)
    print("Los numeros pares son:", pares)
    impares=sorted(impares)
    print("Los numeros impares son:", impares)



if __name__=='__main__':
    print(separar())
