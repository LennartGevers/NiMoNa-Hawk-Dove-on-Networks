def apply_heat_equation(x_1, x_2, a, dist):
    return a* (( x_2 - x_1) / dist)

def normalize_nodes(nodes):
    #normalizes the vector of hawks and doves of all nodes in respect to the normalization condition
    #that hawks + doves = 1 while maintaining the ratio of hawks and doves in a node.
    
    for node in nodes:

        value_hawk, value_dove = node.get_value()
        sum_hawk_dove = value_dove + value_hawk
        node.set_value(((value_hawk)/ (sum_hawk_dove), (value_dove)/(sum_hawk_dove)))


def heat_equation(nodes, a_hawk, a_dove):

    new_values = []

    for node in nodes:
        hawk_value, dove_value = node.get_value()
        hawk_update = 0
        dove_update = 0

        for connecting_node, distance in node.get_connections():
            connecting_hawk_value, connecting_dove_value = connecting_node.get_value()

            hawk_update += apply_heat_equation(hawk_value, connecting_hawk_value, a_hawk, distance)
            dove_update += apply_heat_equation(dove_value, connecting_dove_value, a_dove, distance)

        new_values.append( (hawk_value + hawk_update, dove_value + dove_update))

    for i in range(0,len(nodes)):
        nodes[i].set_value(new_values[i])

    normalize_nodes(nodes)