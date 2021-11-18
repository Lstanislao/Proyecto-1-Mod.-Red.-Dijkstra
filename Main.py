import sys
import os
import time

from Grafo import Graph


def clearConsole():
    '''Funcion para limpiar la consola'''
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def commonPath(javier, andreina):
    ''' Busca las aristas en comun que recorren Javier y Andreina en su ruta '''
    commonPath = []
    pathJavier = str(javier).split(",")
    pathAndreina = str(andreina).split(",")

    for i in range(len(pathJavier)):
        if(pathJavier[i] in pathAndreina and pathJavier[i-1] in pathAndreina):
            if(pathJavier[i-1] not in commonPath):
                commonPath.append(pathJavier[i-1])
            if(pathJavier[i] not in commonPath):
                commonPath.append(pathJavier[i])

    return commonPath


if __name__ == '__main__':

    # se supone que esto va mas o menos asi
    # se crea el grafo
    g = Graph()

    # posibles destinos
    # 5014.0 Discoteca
    # 5411.0 Bar
    # 5012.0 Cerveceria

    # posibles incicios
    # 5414.0 Javier
    # 5213.0 Andreina

    # se calcula la ruta para javier primero
    # a esto se le pasa por parametro el inicio y fin o sea calle 54 carrera 14
    print()
    print('Cerveceria')
    print()

    # se calcula javier
    javier = g.dijkstra(5414.0, 5012.0)

    print('ruta de javier', javier['route'])
    print('tiempo de javier', javier['minutes'])
    print('timming', javier['time'])
    # aqui se le suma 2 al grafo porque andreina es mas lenta, entonces esto suma 2 a todo el grafo
    g.updateMatrixTo(2)
    # calculo la ruta de andreina
    andreina = g.dijkstra(5213.0, 5012.0)

    print('ruta de andreina', andreina['route'])
    print('tiempo de andreina', andreina['minutes'])
    print('timming', andreina['time'])
    print()

    # esto es para saber con quien se esta usando el grafo
    # last es andreina porque es la ultima que se le hizo la busqueda
    # y el grafo esta a su velocidad
    last = 'andreina'

    # mientras haya alguna ruta en comun
    commonRoute = ['null']
    while(len(commonRoute) != 0):
        # esto saca si hay alguna ruta en comun
        commonRoute = commonPath(javier['route'], andreina['route'])
        # esto bloquea la ruta que tomo javier para que andreina no la tome
        if(javier['minutes'] > andreina['minutes']):
            g.updateAdjMatrix(commonRoute)
            # si se hace mas de un iteracion y el ultimo fue el grafo de javier
            if(last == 'javier'):
                g.updateMatrixTo(-2)
                last = 'andreina'
            andreina = g.dijkstra(5213.0, 5012.0)
        # se bloquea la ruta que tomo javier para que andreina no la tome
        else:
            g.updateAdjMatrix(commonRoute)
            if(last == 'andreina'):
                g.updateMatrixTo(-2)
                last = 'javier'
            javier = g.dijkstra(5414.0, 5012.0)

        # FIXME: la ruta comun nunca esta cambiando
        # se verifica de nuevo que no haya una ruta en comun
        commonRoute = commonPath(javier['route'], andreina['route'])

        print(commonRoute)


    # esto es para saber el timmon no creo que sea necesario idk no lo borres aun comentalo
    if(javier['minutes'] > andreina['minutes']):
        dif = javier['minutes'] - andreina['minutes']
        for i in range(len(andreina['time'])):
            andreina['time'][i] += dif
    else:
        dif = andreina['minutes'] - javier['minutes']
        for i in range(len(javier['time'])):
            javier['time'][i] += dif

    print('ruta de javier', javier['route'])
    print('tiempo de javier', javier['minutes'])
    print('timming', javier['time'])

    print('ruta de andreina', andreina['route'])
    print('tiempo de andreina', andreina['minutes'])
    print('timming', andreina['time'])

    # si se quiere volver a saber otra ruta sin tener que volver a correr
    # g.initMatrix()  resetea la matriz de adyacencia a la inicial para volver a calcular javier y andreina
    # --------------------------------------------------------------------------------
    print()
    print('Discoteca')
    print()
    g.initMatrix()
    javier = g.dijkstra(5414.0, 5014.0)

    # luego se le quita esa ruta a andreina

    g.updateMatrixTo(2)

    andreina = g.dijkstra(5213.0, 5014.0)
    commonRoute = ['null']
    last = 'andreina'
    while(len(commonRoute) != 0):
        commonRoute = commonPath(javier['route'], andreina['route'])
        if(javier['minutes'] > andreina['minutes']):
            g.updateAdjMatrix(commonRoute)
            if(last == 'javier'):
                g.updateMatrixTo(-2)
                print('lol1')
                last = 'andreina'
            andreina = g.dijkstra(5213.0, 5014.0)
        else:
            g.updateAdjMatrix(commonRoute)
            if(last == 'andreina'):
                g.updateMatrixTo(-2)
                last = 'javier'
            javier = g.dijkstra(5414.0, 5014.0)

        commonRoute = commonPath(javier['route'], andreina['route'])

    if(javier['minutes'] > andreina['minutes']):
        dif = javier['minutes'] - andreina['minutes']
        for i in range(len(andreina['time'])):
            andreina['time'][i] += dif
    else:
        dif = andreina['minutes'] - javier['minutes']
        for i in range(len(javier['time'])):
            javier['time'][i] += dif

    print('ruta de javier', javier['route'])
    print('tiempo de javier', javier['minutes'])
    print('timming', javier['time'])

    print('ruta de andreina', andreina['route'])
    print('tiempo de andreina', andreina['minutes'])
    print('timming', andreina['time'])
    # -----------------------------------------------------------------
    print()
    print('Bar')
    print()
    g.initMatrix()
    javier = g.dijkstra(5414.0, 5411.0)

    g.updateMatrixTo(2)
    andreina = g.dijkstra(5213.0, 5411.0)
    last = 'andreina'
    while(len(commonRoute) != 0):
        commonRoute = commonPath(javier['route'], andreina['route'])
        print(commonRoute)
        if(javier['minutes'] > andreina['minutes']):
            g.updateAdjMatrix(commonRoute)
            if(last == 'javier'):
                g.updateMatrixTo(-2)
                last = 'andreina'
            andreina = g.dijkstra(5213.0, 5411.0)
        else:
            g.updateAdjMatrix(commonRoute)
            if(last == 'andreina'):
                g.updateMatrixTo(-2)
                last = 'javier'
            javier = g.dijkstra(5414.0, 5411.0)

        commonRoute = commonPath(javier['route'], andreina['route'])

    if(javier['minutes'] > andreina['minutes']):
        dif = javier['minutes'] - andreina['minutes']
        for i in range(len(andreina['time'])):
            andreina['time'][i] += dif
    else:
        dif = andreina['minutes'] - javier['minutes']
        for i in range(len(javier['time'])):
            javier['time'][i] += dif

    print('ruta de javier', javier['route'])
    print('tiempo de javier', javier['minutes'])
    print('timming', javier['time'])

    print('ruta de andreina', andreina['route'])
    print('tiempo de andreina', andreina['minutes'])
    print('timming', andreina['time'])


sys.exit(0)
