import numpy as np

def constant_harm(c):
    def harm(t, value_vector, position):
        return c

    return harm

def constant_reward(v):
    def reward(t, value_vector, position):
        return v

    return reward

def periodic_reward(a, T, a_0):
    def reward(t, value_vector, position):
        return a * np.sin(2 * np.pi * (t/T)) + a_0

    return reward

def periodic_reward_heigth_amplitude(a, T, a_0):
    def reward(t, value_vector, position):
        return a*(position[0]) * np.sin(2 * np.pi * (t/T)) + a_0

    return reward