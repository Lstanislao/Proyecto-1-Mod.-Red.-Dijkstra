import sys
import os
import time

from Grafo import Graph
from Menu import header, menu, gps, aboutUs, contact, credits, routes, aboutHeader, contactHeader




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
    clearConsole()
    header()
    menu()
    optionMenu = int(input("Ingrese su opción deseada: \n"))
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

    while optionMenu != 0:

        if optionMenu == 1:
            clearConsole()
            header()
            gps()
            optionGps = int(input("Ingrese su opción deseada: \n"))

            while optionGps != 0:
                if optionGps == 1:

                    # se calcula la ruta para javier primero
                    # a esto se le pasa por parametro el inicio y fin o sea calle 54 carrera 14
                    clearConsole()
                    routes()
                    print('Cervecería Mi Rolita: Calle 50 con Carrera 12')
                    print()
                    g.initMatrix()
                    # se calcula javier
                    javier = g.dijkstra(5414.0, 5012.0)
                    # aqui se le suma 2 al grafo porque andreina es mas lenta, entonces esto suma 2 a todo el grafo
                    g.updateMatrixTo(2)
                    # calculo la ruta de andreina
                    andreina = g.dijkstra(5213.0, 5012.0)

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
                        # se verifica de nuevo que no haya una ruta en comun
                        commonRoute = commonPath(javier['route'], andreina['route'])

                    # esto es para saber el timmon no creo que sea necesario idk no lo borres aun comentalo
                    if(javier['minutes'] > andreina['minutes']):
                        dif = javier['minutes'] - andreina['minutes']
                        for i in range(len(andreina['time'])):
                            andreina['time'][i] += dif
                    else:
                        dif = andreina['minutes'] - javier['minutes']
                        for i in range(len(javier['time'])):
                            javier['time'][i] += dif

                    print('Ruta de Javier', javier['route'])
                    print('\nTiempo de Javier', javier['minutes'])
                    print('\nTimming', javier['time'])

                    print('\n\nRuta de Andreina', andreina['route'])
                    print('\nTiempo de Andreina', andreina['minutes'])
                    print('\nTimming', andreina['time'])
                    print('_______________________________________________________________________________')

                    # si se quiere volver a saber otra ruta sin tener que volver a correr
                    # g.initMatrix()  resetea la matriz de adyacencia a la inicial para volver a calcular javier y andreina

                elif optionGps == 2:

                    clearConsole()
                    routes()
                    print('Discoteca The Darkness: Carrera 14 con Calle 50')
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
                        print(commonRoute)
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

                    print('\nRuta de Javier', javier['route'])
                    print('\nTiempo de Javier', javier['minutes'])
                    print('\nTimming', javier['time'])

                    print('\n\nRuta de Andreina', andreina['route'])
                    print('\nTiempo de Andreina', andreina['minutes'])
                    print('\nTimming', andreina['time'])
                    print('_______________________________________________________________________________')


                elif optionGps == 3:

                    clearConsole()
                    routes()
                    print('Bar La Pasión: Calle 54 con Carrera 11')
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

                    print('\nRuta de Javier', javier['route'])
                    print('\nTiempo de Javier', javier['minutes'])
                    print('\nTimming', javier['time'])

                    print('\n\nRuta de Andreina', andreina['route'])
                    print('\nTiempo de Andreina', andreina['minutes'])
                    print('\nTimming', andreina['time'])
                    print('_______________________________________________________________________________')


                else:
                    clearConsole()
                    print('Opción invalida\n')
                    header()
                    gps()
                    optionGps = int(input("Ingrese su opción deseada: \n"))
                gps()
                optionGps = int(input("Ingrese su opción deseada: \n"))
                clearConsole()

        elif optionMenu == 2:
            clearConsole()
            aboutHeader()
            aboutUs()
            optionAboutUs = int(input("Ingrese su opción deseada: \n"))

            while optionAboutUs != 0:
                clearConsole()
                print('Opción invalida\n')
                aboutHeader()
                aboutUs()
                optionAboutUs = int(input("Ingrese su opción deseada: \n"))

            clearConsole()

        elif optionMenu == 3:
            clearConsole()
            contactHeader()
            contact()
            optionContact = int(input("Ingrese su opción deseada: \n"))

            while optionContact != 1:
                print('Opción invalida\n')
                optionContact = int(input("Ingrese su opción deseada: \n"))
            clearConsole()
            print('______________________________________________________________________________')
            print('|¡Gracias por tu mensaje! Te contactaremos en cuanto llegue la luz al cuarto  |\n')
            print('|de servidores. ¡Por parte del equipo de GPS Cupido te deseamos un feliz día! |\n')
            print('|_____________________________________________________________________________|')

        else:
            print('Opción invalida\n')
        header()
        menu()
        optionMenu = int(input("Ingrese su opción deseada: \n"))
    
    clearConsole()
    header()
    credits()
sys.exit(0)
