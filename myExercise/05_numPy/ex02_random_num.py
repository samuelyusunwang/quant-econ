# Random number generator 

import numpy as np
import matplotlib.pyplot as plt

class discreteRV:
    q = 1
    
    def __init__(self, q):
        self.q = q
    
    def draw0(self):
        interval = np.cumsum(self.q)
        U = np.random.uniform()
        k = interval.searchsorted(U)
        return k
    
    def draw(self, k):
        rn = []
        for i in range(k):
            rn.append(self.draw0())
        return rn
            

# Test code
q = [0.1, 0.2, 0.3, 0.2, 0.2]
rv = discreteRV(q)
print(rv.draw0())
sample = rv.draw(1000)
print(sample)
plt.hist(sample)
plt.show()
        
    
        
    
    