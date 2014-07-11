# Use numPy to calculate polynomial value
import numpy as np

def p(x, coeff):
    x_power = np.ones(len(coeff))
    x_power[1:] = x
    x_power = np.cumprod(x_power)
    return np.sum((x_power) * np.array(coeff))


# Test code
coeff = [1, 2, 3, 4, 5]
x = [0, 1, 2, 3]

for xx in x:
    print(p(xx,coeff))
    
