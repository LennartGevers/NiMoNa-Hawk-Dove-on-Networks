from src.structure.environment import generate_environment, normalize_nodes
from src.structure.visualize import visualize

from src.model.replicator_dynamics.replicator_dynamics import replicator_dynamics
from src.model.replicator_dynamics.payoff_parameter_functions import constant_harm, constant_reward

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

harm_function = constant_harm(1.5)
reward_function = constant_reward(1)

for t in range(0,T):
    replicator_dynamics(environment, t, reward_function, harm_function, 3)

