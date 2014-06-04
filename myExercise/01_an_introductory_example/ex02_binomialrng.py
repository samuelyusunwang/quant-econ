from random import uniform

def binomial_rv(n,p):
    Y = 0 #binomial randome variable Y
    for i in range(n):
        U = uniform(0,1)
        if U < p:
            Y += 1
    return Y

n = 10
p = 0.5
print(binomial_rv(n,p))

    