import sys
import os
import time

from Grafo import Graph
from Menu import header, menu, gps, aboutUs, contact, credits, routes, aboutHeader, contactHeader
from MostrarGrafo import ShowGraph

# SE DEBE CERRAR LA VENTANA DE LA REPRESENTACION GRAFICA DEL GRAFO PARA CONTINUAR EL PROGRAMA

def clearConsole():
    '''Funcion para limpiar la consola'''
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def commonPath(javier, andreina):
    ''' Busca las aristas en comun que recorren Javier y Andreina en su ruta '''
    
    commonPath = []
    pathJavier = str(javier).split(" --> ")
    pathAndreina = str(andreina).split(" --> ")

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

    # Se muestra el menu principal
    menu()
    optionMenu = input("Ingrese su opción deseada: \n")
    
    # Se crea el grafo
    g = Graph()

    # Posibles destinos
    # 5014.0 Discoteca
    # 5411.0 Bar
    # 5012.0 Cerveceria

    # Posibles inicios
    # 5414.0 Javier
    # 5213.0 Andreina

    while optionMenu != '0':

        # Si se elige ver las rutas
        if optionMenu == '1':
            clearConsole()
            header()
            gps()
            optionGps = input("Ingrese su opción deseada: \n")

            # Se guardan los nodos de origen de Javier y Andreina
            javierOrigin = 5414.0
            andreinaOrigin = 5213.0

            while optionGps != '0':
                clearConsole()
                routes()
                commonRoute = ['null']
                if optionGps == '1':
                    # Se asignan los valores para la Discoteca The Darkness 
                    
                    destinyName = 'Discoteca The Darkness: Carrera 14 con Calle 50\n'
                    destinyNode = 5014.0

                elif optionGps == '2':
                    # Se asignan los valores para el Bar La Pasion 
                    
                    destinyName = 'Bar La Pasión: Calle 54 con Carrera 11\n'
                    destinyNode = 5411.0

                elif optionGps == '3':
                    # Se asignan los valores para el Bar La Pasion 
                    
                    destinyName = 'Cervecería Mi Rolita: Calle 50 con Carrera 12\n'
                    destinyNode = 5012.0

                else:
                    clearConsole()
                    print('Opción inválida\n')
                    header()
                    gps()
                    optionGps = input("Ingrese su opción deseada: \n")
                
                clearConsole()

                # Se muestra el destino de la ruta
                routes()
                print(destinyName)
                print()

                # Se resetea la matriz de adyacencia a la inicial
                g.initMatrix()

                # Se busca la ruta de costo minimo para Javier hacia el destino elegido
                javier = g.dijkstra(javierOrigin, destinyNode)

                # Se suma 2 a las posiciones de la matriz de adyacencia porque Andreina es 2 minutos
                # mas lenta
                g.updateMatrixTo(2)

                # Se busca la ruta de costo minimo para Andreina hacia el destino elegido
                andreina = g.dijkstra(andreinaOrigin, destinyNode)

                # Esta variable es para saber con quien se esta usando el grafo
                # Empieza en andreina porque es la ultima que se le hizo la busqueda
                # y el grafo esta a su velocidad
                last = 'andreina'

                # Se procedera a evaluar si recorren aristas en comun y de hacerlo, se cambian 
                # sus rutas hasta que no tengan porque no pueden ser vistos caminando juntos

                # Mientras haya alguna ruta en comun
                while(len(commonRoute) != 0):
                    # Se busca su ruta en comun
                    commonRoute = commonPath(javier['route'], andreina['route'])
                   
                    # Se bloquea la ruta en comun en la matriz adyacencia para que no se 
                    # puedan tomar en cuenta esas aristas en la nueva busqueda
                    g.updateAdjMatrix(commonRoute)
                    
                    # Al que se haya tardado menos, se le busca una nueva ruta que no 
                    # coincida con la del otro
                    if(javier['minutes'] > andreina['minutes']):
                        #Si Andreina se tardo menos
                        
                        # En caso de que se haya analizado el grafo de Javier de ultimo
                        if(last == 'javier'):
                            # Se actualiza la matriz de adyacencia a los valores para Andreina
                            g.updateMatrixTo(2)
                            last = 'andreina'
                        # Se calcula nuevamente la ruta de costo minimo para Andreina
                        andreina = g.dijkstra(andreinaOrigin, destinyNode)
                    else:
                        # Si Javier se tardo menos

                        # En caso de que se haya analizado el grafo de Andreina de ultimo
                        if(last == 'andreina'):
                            # Se actualiza la matriz de adyacencia a los valores para Javier
                            g.updateMatrixTo(-2)
                            last = 'javier'
                        # Se calcula nuevamente la ruta de costo minimo para Javier
                        javier = g.dijkstra(javierOrigin, destinyNode)

                    # Se verifica de nuevo que no haya una ruta en comun
                    commonRoute = commonPath(javier['route'], andreina['route'])


                # Con las rutas ya listas, se ve quien debe salir antes y por cuanto tiempo
                if(javier['minutes'] > andreina['minutes']):
                    dif = javier['minutes'] - andreina['minutes']
                    firstOut = 'Javier'
                    lastOut = 'Andreina'

                    for i in range(len(andreina['time'])):
                        andreina['time'][i] += dif
                else:
                    dif = andreina['minutes'] - javier['minutes']
                    firstOut = 'Andreina'
                    lastOut = 'Javier'

                    for i in range(len(javier['time'])):
                        javier['time'][i] += dif

                # Se muestran los resultados para Javier
                print('Ruta de Javier', javier['route'])
                print('\nTiempo de Javier', javier['minutes'])
                print('\nTimming', javier['time'])

                # Se muestran los resultados para Andreina
                print('\n\nRuta de Andreina', andreina['route'])
                print('\nTiempo de Andreina', andreina['minutes'])
                print('\nTimming', andreina['time'])

                # Se muestra quien debe salir antes y por cuanto tiempo
                if javier['minutes'] == andreina['minutes']:
                    print('\n\nPara que lleguen exactamente al mismo momento, Javier y Andreina deben salir al mismo tiempo')
                else:
                    print('\n\nPara que lleguen exactamente al mismo tiempo, {0} debe salir {1} minutos antes que {2}'.format(firstOut, dif, lastOut))
                print('_______________________________________________________________________________')

                # si se quiere volver a saber otra ruta sin tener que volver a correr
                # g.initMatrix()  resetea la matriz de adyacencia a la inicial para volver a calcular javier y andreina

                # Se muestra el grafo con las rutas de Javier y Andreina. Comentar linea si no se quiere graficar
                # Tomar en cuenta que el tiempo entre los nodos mostrados son los de Javier, los Andreina son esos mas 2
                ShowGraph(javier['route'], andreina['route'], 'Camino de costo mínimo a ' + destinyName)

                gps()
                optionGps = input("Ingrese su opción deseada: \n")
                clearConsole()

        # Si se elige ver sobre nosotros
        elif optionMenu == '2':
            clearConsole()
            aboutHeader()
            aboutUs()
            optionAboutUs = input("Ingrese su opción deseada: \n")

            while optionAboutUs != '0':
                clearConsole()
                print('Opción inválida\n')
                aboutHeader()
                aboutUs()
                optionAboutUs = input("Ingrese su opción deseada: \n")

            clearConsole()

        # Si se elige contactar
        elif optionMenu == '3':
            clearConsole()
            contactHeader()
            contact()
            optionContact = input("Ingrese su opción deseada: \n")

            while optionContact != '0' and optionContact != '1':
                if optionContact == '1':
                    clearConsole()
                    print('______________________________________________________________________________')
                    print('|¡Gracias por tu mensaje! Te contactaremos en cuanto llegue la luz al cuarto  |\n')
                    print('|de servidores. ¡Por parte del equipo de GPS Cupido te deseamos un feliz día! |\n')
                    print('|_____________________________________________________________________________|')
                else:
                    print('Opción inválida\n')
                    optionContact = input("Ingrese su opción deseada: \n")
            
        else:
            print('Opción inválida\n')
        header()
        menu()
        optionMenu = input("Ingrese su opción deseada: \n")
    
    clearConsole()
    header()
    credits()
sys.exit(0)
