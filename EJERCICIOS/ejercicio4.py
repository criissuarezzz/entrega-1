class Ej4:
    def ordenar(c):
        return c['prioridad']
    def estructura_cola():
        cola= [
            {'tarea 3': 'ir a clase', 'prioridad':'3'},
            {'tarea 1': 'levantarme', 'prioridad':'1'},
            {'tarea 2': 'comer', 'prioridad':'2'}
        ]
        cola.sort(key=ordenar)
        for i in cola:
            print(i)

if __name__=='__main__':
    print(Ej4.estructura_cola())