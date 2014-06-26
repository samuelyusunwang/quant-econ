# A functin that find if every elt in seq_a is an elt in seq_b: list/tuple/string

def seq_compare(seq_a, seq_b):
    for x in seq_a:
        if x not in seq_b:
            return False
    return True


# Test code
s1 = [1,2,3,4,5,6,7]
s2 = [1,2,3,4,5,6,7,8,9,10]

print( seq_compare(s1,s2) )
print( seq_compare(s2,s1) )