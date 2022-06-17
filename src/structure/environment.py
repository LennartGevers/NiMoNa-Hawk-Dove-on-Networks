import numpy as np

from src.structure.node import network_node
from src.structure.visualize import visualize
from src.model.normalization import norm_environment

def update_connections(new_node, nodes, max_dist):
    for node in nodes:
        distance = node.distance(new_node)
        if (distance <= max_dist):
            node.add_connection(new_node, distance)

def generate_quadratic_environment(n_height, n_width, seed=False):
    if seed:
        np.random.seed(seed)

    nodes_arr = []

    x_diff = 1/(n_width-1)
    y_diff = 1/(n_height-1)
    

    for x in range(0, n_width):
        nodes_arr.append([])

        for y in range(0, n_height):
            val_i = np.random.random()

            #Value Vector (x_1, x_2) where x_1 is hawks and x_2 is doves
            val_vector = (val_i, 1-val_i)

            nodes_arr[x].append( network_node(x*x_diff, y*y_diff, val_vector))

            if(x > 0):
                nodes_arr[x][y].add_connection(nodes_arr[x-1][y], x_diff)

            if(y > 0):
                nodes_arr[x][y].add_connection(nodes_arr[x][y-1], y_diff)

        
        #Verbindung der Knoten die an den auesseren Seiten des Netzwerkes liegen
        for x in range(0, len(nodes_arr)):
            nodes_arr[x][0].add_connection(nodes_arr[x][-1], y_diff)
        
        for y in range(0, len(nodes_arr)):
            nodes_arr[0][y].add_connection(nodes_arr[-1][y], x_diff)

        #Aus 2D Liste hintereinandergekettete 1D Liste machen
        #Gitterpostionen bleiben erhalten.

        nodes = []
    for line in nodes_arr:
        nodes = nodes + line
    return nodes


def generate_random_environment(count, max_dist, seed=False):
    if seed:
        np.random.seed(seed)
    
    nodes = []

    for i in range(0, count):
        x_i = np.random.random()
        y_i = np.random.random()

        val_i = np.random.random()

        #Value Vector (x_1, x_2) where x_1 is hawks and x_2 is doves

        val_vector = (val_i, 1-val_i)

        node_i = network_node(x_i, y_i, val_vector)

        update_connections(node_i, nodes, max_dist)

        nodes.append(node_i)

    norm_environment(nodes)

    return nodes

def get_minimum_distance(nodes):
    min_dists = [np.sqrt(2)]
    for node in nodes:
        if(len(node.get_connections()) > 0):
            min_dists.append(min([distance for _,distance in node.get_connections()]))

    return min(min_dists)


        