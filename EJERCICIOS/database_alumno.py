



class Alumno:

    def __init__(self, cadena):
        self.cadena=cadena

    lista=[]

    @staticmethod
    def buscar_cadena(cadena):
        for cadena in enumerate(Alumno.lista):
            if cadena == cadena:
                return cadena

    @staticmethod
    def agregar_cadena(cadena):
        Alumno.lista.append(cadena)
        return cadena

    @staticmethod
    def transformar_cadena(cadena):
        legible=cadena[::-1]
        frase = legible.split(",")
        Nota_de_nota=frase[0]
        Nombre_Apellido=frase[1]
        alumno=Alumno(cadena)
        return f'{Nombre_Apellido} ha sacado un {Nota_de_nota}'

    @staticmethod
    def eliminar_cadena(cadena):
        for i, cadena in enumerate(Alumno.lista):
            if cadena == cadena:
                del Alumno.lista[i]
                return cadena

# Experimentacion
nombre1=Alumno("zeréP nauJ,01")
print(Alumno.transformar_cadena(nombre1.cadena))


