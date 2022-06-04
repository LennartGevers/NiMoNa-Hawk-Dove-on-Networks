def constant_harm(c):
    def harm(t, value_vector, position):
        return c

    return harm

def constant_reward(v):
    def reward(t, value_vector, position):
        return v

    return reward