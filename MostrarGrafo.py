import networkx as nx

def ShowGraph():
    # Se crea el grafo
    g = nx.Graph()

    # Se agregan los nodos en su posicion correspondiente
    
    carrera = 15

    for i in range(6):
        calle = 50
        for j in range(6):

            g.add_node(str(calle) + str(carrera), pos=(i,j))

            calle += 1
        
        carrera -= 1

    # Se agregan las aristas entre sus nodos adyacentes
    calle = 50
    carrera = 15

    for i in range(6):
        carreraW = 5
        if carrera in (12,13,14):
            carreraW = 7 
        
        for j in range(6):
            calleW = 5
            if calle == 51:
                calleW = 10 
            if carrera - 1 >= 10:
                g.add_edge(str(calle) + str(carrera), str(calle) + str(carrera - 1),  weight=calleW)

            if calle + 1 <= 55:
                g.add_edge(str(calle) + str(carrera), str(calle + 1) + str(carrera),  weight=carreraW)

            calle += 1
        
        carrera -= 1
  