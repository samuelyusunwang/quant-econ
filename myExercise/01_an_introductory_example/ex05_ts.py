from pylab import plot, show, legend
from random import normalvariate

N = 200
alpha = 0.9

x = [0]
for i in range(N):
    x.append(alpha*x[i]+normalvariate(0,1))

plot(x,'b-', label="ts")
legend()
show()