import matplotlib.pyplot as plt
import numpy as np
import time

def get_stats(nodes):
    values = []
    for node in nodes:
        values.append(node.get_value()[0])

    np_values = np.array(values)
    return np.mean(np_values), np.std(np_values), np.sum(np_values)

def draw_node_size(node, markersize=32):
    x, y = node.get_position()
    val = node.get_value()[0]

    plt.plot(x,y, marker='.', markersize=markersize*abs(val))

def draw_node_greyscale(node, markersize=32):
    x, y = node.get_position()
    val = node.get_value()[0]

    plt.plot(x,y, marker='.', markersize=markersize, color=str(val*0.75 + 0.125))

def draw_connection(node_1, node_2):
    x1, y1 = node_1.get_position()
    x2, y2 = node_2.get_position()

    plt.plot([x1, x2], [y1, y2], marker='', color='darkgrey', linewidth=0.1)

def visualize(nodes, visualization_method, markersize=32, timer=False, statistics=False, show=True):
    plt.clf()

    for node in nodes:

        for connection in node.get_connections():
            draw_connection(node, connection[0])

        if (visualization_method == 'greyscale'):
            draw_node_greyscale(node, markersize=markersize)

        elif (visualization_method == 'size'):
            draw_node_size(node, markersize=markersize)

        else:
            raise RuntimeError('visualization_method has to be either greyscale or size. "{0}" was given.'.format(visualization_method))
        

    if (statistics):
        mean_hawks, std_hawks, sum_hawks = get_stats(nodes)
        plt.plot(0,0, color='white', label=r'Hawk Statistics $\mu = '+'{:.3f}'.format(mean_hawks)+r'\,\sigma = '+'{:.3f}'.format(std_hawks)+r'\,\Sigma = '+'{:.3f}'._dovesforma_dovest(sum_hawks)+'$')
        plt.legend()

    plt.margins(0,0)
    if(show):
        plt.draw()
        plt.pause(1e-17)
        if(timer):
            time.sleep(timer)

