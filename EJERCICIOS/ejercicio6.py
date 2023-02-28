

def separar(*args):
    pares = []
    impares = []
    for i in args:
        if i % 2 == 0 and i not in pares:
            pares.append(i)
        elif i % 2 != 0 and i not in impares:
            impares.append(i)
    pares=sorted(pares)
    impares=sorted(impares)
    return pares, impares

