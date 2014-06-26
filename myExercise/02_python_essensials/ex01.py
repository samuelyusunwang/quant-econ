# inner product

def inner_prod(x_vals, y_vals):
    return sum([x*y for (x,y) in zip(x_vals, y_vals)])

def count_even_num(x_vals):
    return sum([1-x%2 for x in x_vals])
    
def count_even_pairs(pairs):
    return sum([x%2==0 & y%2==0 for (x,y) in pairs])

# Test the code
x = range(5)
y = range(5,10)
print(inner_prod(x,y))

x = [1, 4, 8, 2, 3, 5, 7, 9]
print(count_even_num(x))

pairs = ((2,5), (4,2), (9,8), (12,10))
print(count_even_pairs(pairs))