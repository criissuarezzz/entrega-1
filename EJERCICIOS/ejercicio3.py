class Ejercicio3:
    lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
    print("La lista 1 es:", lista_1)

    lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
    print("La lista 2 es:", lista_2)

    def lista(lista_1, lista_2):
        lista_3=[]
        for item in lista_1:
            if item in lista_2 and item not in lista_3:
                lista_3.append(item)
        return lista_3

    print(lista())
            