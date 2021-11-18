import networkx as nx
import matplotlib.pyplot as plt

def ShowGraph(ruta_javier, ruta_andreina):
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
        calle = 50
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

    # print(g.nodes(data=True))
    # print(g.edges(data=True))

    pos = nx.get_node_attributes(g, 'pos')
    edge_labels = nx.get_edge_attributes(g, 'weight')
    # print(edge_labels)

    # javier = 5414
    # andreina = 5213
    the_darkness = "5014"
    la_pasion = "5411"
    mi_rolita = "5012"

    # Definiendo estilos para las aristas
    nx.draw_networkx_edge_labels(g, pos, edge_labels, font_size=9)
    nx.draw(g, pos, with_labels=True, node_size=750, width=2, font_size=10)
    
    # Definiendo estilos para lugares de encuentro
    nx.draw_networkx_nodes(g,pos, nodelist=[the_darkness, la_pasion, mi_rolita], node_size=750, node_color="pink")
   
    # SI SE QUIEREN DIFERENTES COLORES IDK
    # Definiendo estilos para nodo de Bar La Pasion
    # nx.draw_networkx_nodes(g,pos, nodelist=[la_pasion], node_size=900, node_color="pink")
    # # Definiendo estilos para nodo de Cerveceria Mi Rolita
    # nx.draw_networkx_nodes(g,pos, nodelist=[mi_rolita], node_size=900, node_color="yellow")
   
    # TODO: cambiar color de las aristas
    # Se modifica el color del camino de Javier
    nx.draw_networkx_nodes(g,pos, nodelist=ruta_javier.split(" --> ")[:-1], node_size=750, node_color="green")
    # Se modifica el color del camino de Andreina
    nx.draw_networkx_nodes(g,pos, nodelist=ruta_andreina.split(" --> ")[:-1], node_size=750, node_color="orange")
   
    
    plt.title('Ruta de costo mínimo')
    plt.show()

# ShowGraph('5414 --> 5413 --> 5412 --> 5312 --> 5212 --> 5112 --> 5012', '5213 --> 5113 --> 5013 --> 5012')


  