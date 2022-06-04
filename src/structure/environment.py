import numpy as np

from node import network_node
from visualize import visualize

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

        #Value Vector (x_1, x_2) where x_1 is doves and x_2 is hawks

        val_vector = (val_i, 1 - val_i)

        node_i = network_node(x_i, y_i, val_vector)

        update_connections(node_i, nodes, max_dist)

        nodes.append(node_i)


    return nodes

        