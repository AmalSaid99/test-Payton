#matrix (index 1)
matrix= [[2,5,1],
         [4,9,0],
         [11,6,7]]
print(matrix[1])
#marix (index 1, first No)
matrix= [[2,5,1],
         [4,9,0],
         [11,6,7]]
print(matrix[1][1])
#multiply (row*column)
matrix= [[2,5,1],
         [4,9,0],
         [11,6,7]]
for i in range(len(matrix)): #ROWS
    for j in range(len(matrix)): #COLUMNS
        print(matrix[i][j]*2, end= " ")
    print()

