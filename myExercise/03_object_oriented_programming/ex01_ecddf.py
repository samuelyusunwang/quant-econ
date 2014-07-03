# empirical cumulative distribution function (ecdf)

class ECDF:
    
    observations = 0
    
    def __init__(self, data_sample):
        self.observations = data_sample
    
    def __call__(self, x):
        n = len(self.observations)
        return 1/n * sum([data<=x for data in self.observations])
    


# Test code
from random import uniform
samples = [uniform(0,1) for i in range(10)]
F = ECDF(samples)
print(F(0.5))

F.observations = [uniform(0,1) for i in range(1000)]
print(F(0.5))