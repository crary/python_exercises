# Print heading
print('  | 1  2  3  4  5  6  7  8  9 10')
print(str('-')*2 + '+' + str('-')*31)

#Loop over numbers 1 to 10
for column in range(1,11):
    print(str(column).rjust(2) + '|', end='')

    for row in range(1,11):
        print(str(row*column).rjust(2) + ' ', end='')
    print()

