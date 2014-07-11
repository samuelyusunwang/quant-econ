# empirical cumulative distribution function (ecdf)

import numpy as np
import matplotlib.pyplot as plt


class ECDF:
    
    observations = 0
    
    def __init__(self, data_sample):
        self.observations = np.asarray(data_sample)
    
    def __call__(self, x):
        return np.mean(self.observations <= x)
    
    def plot(self, a=None, b=None):
        # if [a, b] is not specified
        if not a:
            a = self.observations.min() - self.observations.std()
        if not b:
            b = self.observations.max() + self.observations.std()     
        
        # generate plot
        x = np.linspace(a,b,100)
        f = np.vectorize(self.__call__)
        plt.plot(x, f(x))
        plt.show()
        


# Test code
samples = np.random.rand(10)
F = ECDF(samples)
print(F(0.5))

F.observations = np.random.rand(1000)
print(F(0.5))

F.plot()