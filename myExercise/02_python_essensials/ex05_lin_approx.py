# linear approximate and get f(x)

def linapprox(f, a, b, n, x):
    # f: the function
    # a, b: interval [a, b]
    # n: the number of the grids
    # x: input a<x<b
    
    # check feasibility
    if x < a or x > b:
        return 'Error x is not in [a,b]'
    # define n grid points
    xx = [a+(b-a)/(n-1)*i for i in range(n)]
    # find the index that x
    for i in range(n):
        if xx[i] == x:
            return f(xx[i])
        if xx[i] > x: 
            break
        
    k = (f(xx[i])-f(xx[i-1])) / (xx[i]-xx[i-1])
    return k*(x-xx[i-1]) + f(xx[i-1])
    

# Test Code
print( linapprox(lambda x: x**3, 0, 9, 100, 1) )
    
    





    