import numpy as np

def _get_payoff_matrix(reward, harm):

    return np.array([
        [ 0.5*(reward-harm),    reward    ],
        [0,                     0.5*reward]
        ])

def _replicate(dove_value, reward, harm, b=0):
    x = np.array(1 - dove_value, dove_value)

    M = _get_payoff_matrix(reward, harm)

    payoffs = M.dot(x)
    avg_payoffs = x.dot(payoffs)
    normed_payoffs = (payoffs + b)/ (avg_payoffs + b)

    x = x*normed_payoffs

    return (x[0], x[1])

def replicator_dynamics(nodes, t, reward_function, harm_function, b=0):

    for node in nodes:
        value_vector = node.get_values()
        position = node.get_position()

        node.set_values( _replicate( value_vector[1], 
                                    reward_function(t, value_vector, position),
                                    harm_function(t, value_vector, position), b=b))

    

        

