def apply_heat_equation(x_1, x_2, a, dist):
    return a* (( x_2 - x_1) / dist)

def normalize_node(node_values):
    #normalizes the vector of hawks and doves of all nodes in respect to the normalization condition
    #that hawks + doves = 1 while maintaining the ratio of hawks and doves in a node.
    
    value_hawk, value_dove = node_values
    sum_hawk_dove = value_dove + value_hawk
    return((value_hawk)/ (sum_hawk_dove), (value_dove)/(sum_hawk_dove))


def heat_equation(nodes, a_hawk, a_dove, minimum_distance):

    new_values = []

    for node in nodes:
        hawk_value, dove_value = node.get_value()
        hawk_update = 0
        dove_update = 0

        n_connections = len(node.get_connections())

        if(n_connections):

            for connecting_node, distance in node.get_connections():
                connecting_hawk_value, connecting_dove_value = connecting_node.get_value()

                hawk_update += apply_heat_equation(hawk_value, connecting_hawk_value, a_hawk, distance/minimum_distance)
                dove_update += apply_heat_equation(dove_value, connecting_dove_value, a_dove, distance/minimum_distance)

            new_values.append( (hawk_value*(1 + hawk_update/n_connections), dove_value*(1 + dove_update/n_connections)))

        else:
            new_values.append( (hawk_value, dove_value))

    for i in range(0,len(nodes)):
        nodes[i].set_value(normalize_node(new_values[i]))

    