import numpy as np
from src.model.normalization import norm_environment

def _get_payoff_matrix(reward, harm):

    return np.array([
        [ 0.5*(reward-harm),    reward    ],
        [0,                     0.5*reward]
        ])

def _replicate(value__vector, reward, harm, n, b=0):
    x = np.array(value__vector)
    M = _get_payoff_matrix(reward, harm)

    payoff_coeffs = M.dot(x)
    payoffs = (payoff_coeffs + b)*(1-0.05*np.sum(x))

    x = x*payoffs

    return (x[0], x[1])

def replicator_dynamics(nodes, t, reward_function, harm_function, b=0):

    for node in nodes:
        value_vector = node.get_value()
        position = node.get_position()

        node.set_value( _replicate( value_vector, 
                                    reward_function(t, value_vector, position),
                                    harm_function(t, value_vector, position), len(nodes) ,b=b))

    norm_environment(nodes)

    

        

