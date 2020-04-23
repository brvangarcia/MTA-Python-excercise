colums = 5
rows = 5
i = 1
j = 1

while i <= rows:
    print('\n Outer loop #' + str(i))
    while j <= colums:
        print('i =', i, 'j =', j)
        j += 1
    i += 1
    j = 1