# Returns the number of capital letters in the string: use upper()

def count_upper_letter(s):
    # s: a string
    return sum( [x==x.upper() and x.isalpha() for x in s] )

    
    
# Test code
s = 'Sam is a Hero!'
print(s)
print( count_upper_letter(s) )


