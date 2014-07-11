# Calculate Fibonacci numbers by recursive function

def x(t):
    if t == 0 or t == 1:
        return t
    else:
        return x(t-1) + x(t-2)
    

# Test code
for i in range(10):
    print(x(i))