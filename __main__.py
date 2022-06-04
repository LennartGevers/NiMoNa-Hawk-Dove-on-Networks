from src.structure.environment import generate_environment, get_minimum_distance
from src.structure.visualize import visualize

from src.model.replicator_dynamics.replicator_dynamics import replicator_dynamics
from src.model.replicator_dynamics.payoff_parameter_functions import constant_harm, constant_reward

from src.model.heat_equation.heat_equation import heat_equation

#Modeling of the implementation of a heat-equation-like migration of species in the
#hawk dove game.

#Parameters of simulation:

#Seed of simulation
seed = 123

#Number of nodes in the environment
n = 50
#Maximum distance for nodes to be connected to each other
d_max = 0.15

#Number of Time-discrete developments
T = 100

#Developmental Functions and usage per development

#Simulation:
environment = generate_environment(n, d_max, seed=seed)

min_dist = get_minimum_distance(environment)

harm_function = constant_harm(1.5)
reward_function = constant_reward(1)

for t in range(0,T):
    heat_equation(environment, 0.1, 0, min_dist)
    if(t % 20 == 0):
        visualize(environment, 'greyscale', statistics=True)

