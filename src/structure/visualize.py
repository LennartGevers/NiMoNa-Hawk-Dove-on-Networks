import matplotlib.pyplot as plt
import numpy as np
import time

from numpy import block

def get_stats(nodes):
    values = []
    for node in nodes:
        values.append(node.get_value())

    np_values = np.array(values)
    return np.mean(np_values), np.std(np_values), np.sum(np_values)

def draw_node(node, markersize=32):
    x, y = node.get_position()
    val = node.get_value()

    plt.plot(x,y, marker='.', markersize=markersize*abs(val))

def draw_connection(node_1, node_2):
    x1, y1 = node_1.get_position()
    x2, y2 = node_2.get_position()

    plt.plot([x1, x2], [y1, y2], marker='', color='darkgrey', linewidth=0.1)

def visualize(nodes, markersize=32, timer=False, statistics=False, show=True):
    plt.clf()
    for node in nodes:

        for connection in node.get_connections():
            draw_connection(node, connection[0])

        draw_node(node, markersize=markersize)

    if (statistics):
        mean, std, sum = get_stats(nodes)
        plt.plot(0,0, color='white', label=r'$\mu = '+'{:.3f}'.format(mean)+r'\,\sigma = '+'{:.3f}'.format(std)+r'\,\Sigma = '+'{:.3f}'.format(sum)+'$')
        plt.legend()

    plt.margins(0,0)
    if(show):
        plt.draw()
        plt.pause(1e-17)
        time.sleep(0.6)

