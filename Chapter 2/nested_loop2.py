matrix_list = [[' ','Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col5'],['Row 1',1,2,3,4,5],['Row 2',6,7,8,9,10],['Row 3',11,12,13,14,15],['Row 4',16,17,18,19,20],['Row 5',21,22,23,24,25]]

for row in matrix_list:
    column_data = ''
    for column in row:
        column_data = column_data + '\t' + str(column)
    print(column_data)


for row in range(2,13):
    for col in range(2,13):
        print(row * col, end='\t')
    print()

