from structure.environment import generate_environment, normalize_nodes
from structure.visualize import visualize

#Modeling of the implementation of a heat-equation-like migration of species in the
#hawk dove game.

#Parameters of simulation:

#Seed of simulation
seed = 123

#Number of nodes in the environment
n = 100
#Maximum distance for nodes to be connected to each other
d_max = 0.15




environment = generate_environment(n, d_max, seed=seed)
