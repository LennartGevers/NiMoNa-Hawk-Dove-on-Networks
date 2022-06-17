from src.model.normalization import norm_environment

def apply_heat_equation(x_1, x_2, a, dist):
    return a* (( x_2 - x_1) / dist)


def heat_equation(a_hawk, a_dove, minimum_distance):

    def heat_equation_on_nodes(nodes):

        new_values = []

        n = len(nodes)

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

                new_values.append( (hawk_value + hawk_update, dove_value + dove_update))

            else:
                new_values.append( (hawk_value, dove_value) )

        for i in range(0,len(nodes)):
            nodes[i].set_value(new_values[i])
        norm_environment(nodes)

    return heat_equation_on_nodes
    