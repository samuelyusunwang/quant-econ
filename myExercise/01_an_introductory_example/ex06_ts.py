from pylab import plot, show, legend
from random import normalvariate

def ts_plot(N, alpha):
    x = [0]
    for i in range(N):
        x.append(alpha*x[i]+normalvariate(0,1))
    plot( x, label="alpha="+str(alpha) )

ts_plot(200, 0.0)
ts_plot(200, 0.8)
ts_plot(200, 0.98)
legend()
show()