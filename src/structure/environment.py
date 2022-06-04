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

    for i in range(0, count):
        x_i = np.random.random()
        y_i = np.random.random()

        #val_i= ((x_i-0.5)**2 + (y_i-0.5)**2)
        val_i = 0.5 #np.random.random()

        node_i = network_node(x_i, y_i, val_i)

        update_connections(node_i, nodes, max_dist)

        nodes.append(node_i)


    return nodes

        