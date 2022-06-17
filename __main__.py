from src.simulation.simulation import simulation
from src.structure.environment import generate_random_environment, generate_quadratic_environment, get_minimum_distance
from src.structure.visualize import visualize

from src.model.replicator_dynamics.payoff_parameter_functions import constant_harm, constant_reward, periodic_reward

from src.model.migration_dynamics.heat_equation import heat_equation
from src.model.migration_dynamics.no_migratrion import no_migration

from src.simulation.simulation import simulation

import matplotlib.pyplot as plt
import numpy as np

#Modeling of the implementation of a heat-equation-like migration of species in the
#hawk dove game.

environment = generate_quadratic_environment(3, 3, 123)
visualize(environment, 'greyscale')

# simulation = simulation(environment, constant_reward(1), constant_harm(1.5), no_migration)
# simulation.run(256, background_fitness=1)
# simulation.plot()

simulation = simulation(environment, periodic_reward(4, 8, 1), constant_harm(1.5), no_migration)
simulation.run(256, background_fitness=1)
simulation.plot()

plt.axhline(0.333)
plt.axhline(0.666)

plt.show()
