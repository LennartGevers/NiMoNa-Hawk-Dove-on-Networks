from turtle import distance
import numpy as np
from src.structure.node import network_node
from src.structure.visualize import visualize

def update_connections(new_node, nodes, max_dist):
    for node in nodes:
        distance = node.distance(new_node)
        if (distance <= max_dist):
            node.add_connection(new_node, distance)


def generate_environment(count, max_dist, seed=False):
    if seed:
        np.random.seed(seed)
    
    nodes = []

    for _ in range(0, count):
        x_i = np.random.random()
        y_i = np.random.random()

        val_i = np.random.random()

        #Value Vector (x_1, x_2) where x_1 is hawks and x_2 is doves

        val_vector = (val_i, 1 - val_i)

        node_i = network_node(x_i, y_i, val_vector)

        update_connections(node_i, nodes, max_dist)

        nodes.append(node_i)

    return nodes

def get_minimum_distance(nodes):
    min_dists = [np.sqrt(2)]
    for node in nodes:
        if(len(node.get_connections()) > 0):
            min_dists.append(min([distance for _,distance in node.get_connections()]))

    return min(min_dists)


        