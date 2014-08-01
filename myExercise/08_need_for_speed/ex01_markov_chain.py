# Markov Chain

import numpy as np

STATE = np.array([0, 1])

trans_prob = np.array([[0.9, 0.1], [0.2, 0.8]])

def transit(x, trans_prob):
    U = np.random.uniform(0,1)
    k = np.sum(STATE == x)      # get state of x
    prob_step = np.cumsum(trans_prob[k,:])
    y = STATE[prob_step > U]   # assign the next state
    return y[0]

def state_prob(x0, state, n):
    count = 0
    x = x0
    for i in range(n):
        if x == state:
            count += 1
        x = transit(x0, trans_prob)
    return count / n


# Test code
x0 = 1
print( state_prob(x0, 0, 100000) )
