from src.simulation.simulation import simulation
from src.structure.environment import generate_random_environment, generate_quadratic_environment, get_minimum_distance
from src.structure.visualize import visualize

from src.model.replicator_dynamics.payoff_parameter_functions import constant_harm, constant_reward, periodic_reward, periodic_harm, periodic_reward_heigth_amplitude

from src.model.migration_dynamics.heat_equation import heat_equation
from src.model.migration_dynamics.no_migratrion import no_migration
from src.model.migration_dynamics.adjacency_matrix import migration_function, uebergangsmatrix_matrix

from src.simulation.simulation import simulation

import matplotlib.pyplot as plt
import numpy as np

#Modeling of the implementation of a heat-equation-like migration of species in the
#hawk dove game.



environment = generate_quadratic_environment(4, 4, 124)
visualize(environment, 'greyscale')

simulation = simulation(environment, periodic_reward(3, 5, 1), constant_harm(1.5), migration_function(uebergangsmatrix_matrix))
simulation.run(256, background_fitness=1, n_migrate=1, n_replicate=1)
simulation.plot()

#simulation = simulation(environment, periodic_reward_heigth_amplitude(3.5, 8, 1), constant_harm(1.5), no_migration)
#simulation.run(256, background_fitness=0.4)
#simulation.plot()

plt.axhline(0.333)
plt.axhline(0.666)

plt.legend()

plt.show()
