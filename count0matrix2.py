r=0
matrix= [[0,5,1],
         [4,9,0],
         [0,6,0]]
for i in range(len(matrix)): 
    for j in range(len(matrix)):
        if matrix[i][j]==0:
            r+=1
print(r)
