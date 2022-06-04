def harm(c):
    def constant_harm(t, value_vector, position):
        return c

    return constant_harm

def reward(v):
    def constant_reward(t, value_vector, position):
        return v

    return constant_reward