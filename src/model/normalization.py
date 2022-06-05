def sum_environment(nodes):
    return sum([ (node.get_value()[0] + node.get_value()[1]) for node in nodes])

def norm_environment(nodes):
    #Norms the relative population of the environment so that the sum of all species of all nodes is equal to 1.
    #(Instead of a norm applied to each node individually)
    sum_species = sum_environment(nodes)
    
    for node in nodes:
        unnormed_hawk, unnormed_dove = node.get_value()
        node.set_value(unnormed_hawk/sum_species, unnormed_dove/sum_species)