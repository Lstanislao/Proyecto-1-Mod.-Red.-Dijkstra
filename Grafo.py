import numpy as np


class Graph:
    adjMatrix = np.zeros((36, 36))

    def __init__(self):
        for i in range(0, 36):
            for j in range(0, 36):
                self.adjMatrix[i][j] = 999
        self.initMatrix()
    # -----------------------------------------------------------

    def initMatrix(self):
        '''La matriz es simetrica, se rellana el cuadrante de abajo primero proque es mas facil de leer esas coordenadas en
         relacion a la cuadricula, y luego se rellena el cuadrante de arriba que simetrico al de abajo'''
        # Se rellena la distancia de las verticales
        for i in range(0, 30):
            # entra aqui en las verticales que correponden a carrera 14,13,12
            if(i == 2 or i == 3 or i == 4 or i == 8 or i == 9 or i == 10 or i == 14 or i == 15 or i == 16
                    or i == 20 or i == 21 or i == 22 or i == 26 or i == 27 or i == 28):
                self.adjMatrix[i][i+6] = 7
            # en el resto la distancia es 5
            else:
                self.adjMatrix[i][i+6] = 5

        # Se rellena la distancia de las horizontales
        for i in range(0, 35):
            if(i in range(6, 11)):
                self.adjMatrix[i][i+1] = 10
            elif(i != 5 and i != 11 and i != 17 and i != 23 and i != 29):
                self.adjMatrix[i][i+1] = 5

        # Se hace la equivalencia del cuadrante de abajo relleno con el de arriba
        for i in range(36):
            for j in range(i, 36):
                self.adjMatrix[j][i] = self.adjMatrix[i][j]

    # -----------------------------------------------------------

    def initInfoMatrix(self, initialNode):
        # esto crea la matriz de informacion Nodo | dist min | Pre
        infoMatrix = np.zeros((36, 3))
        index = 0
        # se crean los nodos
        for i in range(36):
            if (index == 6):
                index = 0

            if i in range(6):
                infoMatrix[i][0] = 5010 + index

            elif i in range(6, 12):
                infoMatrix[i][0] = 5110 + index

            elif i in range(12, 18):
                infoMatrix[i][0] = 5210 + index

            elif i in range(18, 24):
                infoMatrix[i][0] = 5310 + index

            elif i in range(24, 30):
                infoMatrix[i][0] = 5410 + index

            else:
                infoMatrix[i][0] = 5510 + index

            index += 1

        # se incializa en 0
        for i in range(36):
            infoMatrix[i][1] = 999

        # se coloca el nodo donde se inicia  en distancia 0
        infoMatrix[initialNode][1] = 0

        return infoMatrix

    def dijkstra(self, start, end):
        # Javier
        if(start == 5414.0):
            infoMatrix = self.initInfoMatrix(28)
        else:
            # andreina
            infoMatrix = self.initInfoMatrix(15)

        notVisited = []
        prev = 0

        for i in range(36):
            notVisited.append(infoMatrix[i][0])

        while(len(notVisited) != 0):

            minDistance = 999

            # Se examinan todos los adyacentes no visitados al nodo actual
            # se determina cual es el nodo mas cercano al de inicio que sera el siguiente a viistar
            for i in range(36):

                if(infoMatrix[i][0] in notVisited):

                    if(infoMatrix[i][1] < minDistance):
                        minDistance = infoMatrix[i][1]
                        node = infoMatrix[i][0]

            # Con el nodo mas cercano se procede a visitarlo
            for i in range(36):
                # se busca el nodo
                if(infoMatrix[i][0] == node):
                    # se visita, por lo tanto se saca de la matriz de no visitadis
                    notVisited.remove(node)
                    # se coloca su predecesor
                    prev = node
                    # se examinan sus adyacentes
                    for j in range(36):
                        if(self.adjMatrix[i][j] != 999):
                            # se actualiza el valor si es menor al que se encuentra en la tabla

                            if(infoMatrix[j][1] > self.adjMatrix[i][j] + minDistance):

                                infoMatrix[j][1] = minDistance + \
                                    self.adjMatrix[i][j]

                                infoMatrix[j][2] = prev
        return self.getRoute(infoMatrix, start, end)

    def getRoute(self, infoMatrix, start, destiny):

        output = int(destiny)
        aux = destiny
        time = []

        while(aux != start):
            for i in range(36):
                # Se busca en la matriz de informacion de Javier el nodo actual
                if(infoMatrix[i][0] == aux):

                    if(destiny == infoMatrix[i][0]):
                        minutes = infoMatrix[i][1]
                    # Se actualiza el nodo actual al predecesor del mismo
                    aux = infoMatrix[i][2]

                    # Para quitarle los decimales
                    newPoint = int(aux)
                    time.insert(0, infoMatrix[i][1])
                    # Se agrega el nodo actual en la cadena que se encarga de reconstruir el camino final
                    output = str(newPoint) + "," + str(output)
                    if(aux == start):
                        break
        time.insert(0, 0)

        return ({
            'route': output,
            'minutes': minutes,
            'time': time
        })

    # quita una ruta de la matriz de ady
    def updateAdjMatrix(self, arrayRoute):

        coors = []

        for coord in arrayRoute:
            coors.append(coord[1] + coord[3])

        # Se actualiza la matriz adyacente de forma que aquellas aristas que hayan sido recorridas por Javier no puedan ser recorridas por Andreina
        # el zip esta corrido en coors, coors[1:] proque se necesita es la interseccion entre 2 nodos consecutivos en el camino para act
        # en la matriz
        for x, y in zip(coors, coors[1:]):

            if int(x[0]) == 0:
                coorX = 0
            elif int(x[0]) == 1:
                coorX = 6
            elif int(x[0]) == 2:
                coorX = 12
            elif int(x[0]) == 3:
                coorX = 18
            elif int(x[0]) == 4:
                coorX = 24
            else:
                coorX = 30

            if int(y[0]) == 0:
                coorY = 0
            elif int(y[0]) == 1:
                coorY = 6
            elif int(y[0]) == 2:
                coorY = 12
            elif int(y[0]) == 3:
                coorY = 18
            elif int(y[0]) == 4:
                coorY = 24
            else:
                coorY = 30
            self.adjMatrix[coorX+int(x[1])][(coorY+int(y[1]))] = 999

    def updateMatrixTo(self, num):
        for i in range(0, 36):
            for j in range(0, 36):
                if(self.adjMatrix[i][j] != 999):
                    self.adjMatrix[i][j] += num
    # Borrar al final

    def printGraph(self):
        for i in range(36):
            for j in range(36):
                print(self.adjMatrix[i][j], end=" ")
            print()
