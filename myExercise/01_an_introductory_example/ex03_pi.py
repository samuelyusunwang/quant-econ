from random import uniform
from math import sqrt

N = 1000000  #total number in Monte Carlo Simulation
count = 0
for i in range(N):
    x = uniform(0,1)
    y = uniform(0,1)
    dist = sqrt((x-0.5)**2 + (y-0.5)**2)
    if dist < 0.5:
        count += 1

pi = 4*count/N
print(pi)
