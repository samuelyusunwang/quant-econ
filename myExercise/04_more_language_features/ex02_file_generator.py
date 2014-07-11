def column_iterator(target_file, column_number):
    """A generator function for CSV files.
    When called with a file name target_file (string) and column number
    column_number (integer), the generator function returns a generator
    that steps through the elements of column column_number in file
    target_file.
    """
    # put your code here
    f = open(target_file, 'r')
    for row_data in f:
        count_col = 1
        start = 0
        end = 0  
        for t, x in enumerate(row_data):
            if x == ',' and count_col == column_number:
                end = t
                break
            elif x == ',' and count_col < column_number:
                column_number += 1
                start = t+1
        yield row_data[start:end]


# Test code
dates = column_iterator('test_table.csv', 1)

i = 1
for date in dates:
    print(date)
    if i == 10:
        break
    i += 1
    