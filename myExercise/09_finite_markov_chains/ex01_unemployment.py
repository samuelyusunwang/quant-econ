# Exercise 01: Show the Markov chain converge

import numpy as np
import matplotlib.pyplot as plt

class mc_employment:
    P = np.array([[1,0],[0,1]])
    X0 = 1
    Sample = np.array(X0)
    Prob_unemployment = np.array(X0)
    
    # initialization
    def __init__(self, alpha, beta, x0):
        self.P = np.array([[1-alpha, alpha],
                           [beta,    1-beta] ])
        self.X0 = x0
        
    # sample    
    def simulation(self, n):
        # Simulate the sample
        self.Sample = np.zeros(n)
        self.Sample[0] = self.X0
        for i in range(1, n):
            U = np.random.uniform()
            if self.Sample[i-1] == 0:
                self.Sample[i] = U > self.P[0][0]
            else:
                self.Sample[i] = U > self.P[1][0]
        # Get the average probability of unemployment in sample n        
        self.Prob_unemployment = np.cumsum(self.Sample) / (np.array(range(n))+1)
        
        
# Test code
alpha = 0.3
beta = 0.35
n = 10000
p = beta/(alpha + beta)

mc0 = mc_employment(alpha, beta, 0)
mc0.simulation(n)

mc1 = mc_employment(alpha, beta, 1)
mc1.simulation(n)

plt.plot(range(n), mc0.Prob_unemployment - (1-p), label=r'$X_0=0$') 
plt.plot(range(n), mc1.Prob_unemployment - (1-p), label=r'$X_0=1$')
plt.legend(loc='upper right')

plt.show()

















            
        