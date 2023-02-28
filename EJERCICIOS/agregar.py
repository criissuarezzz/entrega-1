
def agregar_una_vez(lista, elemento):
    if elemento not in lista:
        lista.append(elemento)
    else:
        raise ValueError("Error: Imposible añnadir elementos duplicados=>{}".format(elemento))
    return lista

