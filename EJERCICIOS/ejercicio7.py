class ejercicio7:
    def agregar_una_vez(lista, elemento):
        if elemento not in lista:
            lista.append(elemento)
        else:
            raise ValueError("Error: Imposible añnadir elementos duplicados=>{}".format(elemento))
        return lista

    if __name__ == '__main__':
        print(agregar_una_vez([1, "Hola", 4, "Adiós"], 6))