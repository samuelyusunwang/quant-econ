# use try and except

def countnumber(file_name):
    f = open(file_name, 'r')
    
    total = 0
    for line in f:
        try:
            total += float(line)
        except ValueError:
            pass
    f.close()
    return total

# Test code
print(countnumber('numbers.txt'))
            
        