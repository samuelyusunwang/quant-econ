# use recursive function to solve the root of f(x)=0

import numpy as np

def bisect(f, a, b, tol=10e-5):
    mid = (a+b)/2
    
    if b-a < tol:
        return (a+b)/2
    elif f(mid) < 0:
        return bisect(f, mid, b, tol)
    else:
        return bisect(f, a, mid, tol)
    


# test code
f = lambda x: np.sin(4*(x-0.25)) + x + x**20 - 1
print(bisect(f, 0, 1))