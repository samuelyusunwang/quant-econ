# Definition of the Polynomial class

class Polynomial:
    coefficients = 0
    
    def __init__(self, a):
        self.coefficients = a
    
    def evaluate(self, x):
        return sum( [a*x**i for i, a in enumerate(self.coefficients)] )
    
    def __call__(self, x):
        return self.evaluate(x)
    
    def diff(self):
        self.coefficients = [a*i for i, a in enumerate(self.coefficients[1:], start=1)]
        

# Test code
a = [1, 1, 1, 1, 1]
f = Polynomial(a)
print( f(-1) )
f.diff()
print(f.coefficients)
