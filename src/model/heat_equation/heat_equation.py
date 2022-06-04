def heat_equation(nodes, a_hawks, a_doves):
    

def normalize_nodes(nodes, b = 0):
    #normalizes the vector of hawks and doves of all nodes in respect to the normalization condition
    #that hawks + doves = 1 while maintaining the ratio of hawks and doves in a node.
    
    #Optional backgroundfitness for possibility of negative values.
    
    for node in nodes:

        value_hawk, value_dove = node.get_value()
        sum_hawk_dove = value_dove + value_hawk
        node.set_value(((value_hawk+b)/ (sum_hawk_dove + b), (value_dove + b)/(sum_hawk_dove + b)))