import sys
import os
import time

from Grafo import Graph

# esto limpia la consola


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


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
    javier = g.dijkstra(5414.0, 5012.0)
    print('ruta de javier', javier['route'])
    print('tiempo de javier', javier['minutes'])

    # luego se le quita esa ruta a andreina
    g.updateAdjMatrix(javier['route'])
    andreina = g.dijkstra(5213.0, 5012.0)

    print('ruta de andreina', andreina['route'])
    print('tiempo de andreina', andreina['minutes'])

    # si se quiere volver a saber otra ruta sin tener que volver a correr
    # g.initMatrix()  resetea la matriz de adyacencia a la inicial para volver a calcular javier y andreina
    print()
    print('Discoteca')
    print()
    g.initMatrix()
    javier = g.dijkstra(5414.0, 5014.0)
    print('ruta de javier', javier['route'])
    print('tiempo de javier', javier['minutes'])

    # luego se le quita esa ruta a andreina
    g.updateAdjMatrix(javier['route'])
    andreina = g.dijkstra(5213.0, 5014.0)

    print('ruta de andreina', andreina['route'])
    print('tiempo de andreina', andreina['minutes'])
    # -----------------------------------------------------------------
    print()
    print('Bar')
    print()
    g.initMatrix()
    javier = g.dijkstra(5414.0, 5411)
    print('ruta de javier', javier['route'])
    print('tiempo de javier', javier['minutes'])

    # luego se le quita esa ruta a andreina
    g.updateAdjMatrix(javier['route'])
    andreina = g.dijkstra(5213.0, 5411)

    print('ruta de andreina', andreina['route'])
    print('tiempo de andreina', andreina['minutes'])


sys.exit(0)
