# Ex 02: evaluate polynomial

def p(x, coeff):
    return sum( [a*x**n for (n,a) in enumerate(coeff)])




# Test the function
x = 1.1
coeff = [1, 2, 3, 4, 5, 0]
print( p(x, coeff) )

        