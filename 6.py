matrix1= [[1,2,3],
         [6,7,8]]

matrix2= [[6,1],
         [2,10],
         [0,2]]
def mult_matrix(mtx1,mtx2):
    new_matrix= []
    for row in range(len(mtx1)):
        rows=[]
        for cln in range(len(mtx2)):
           rows.append(mtx1[row][cln]*mtx2[cln][row])
           #for row in range (len(mtx1)):
           rows.append(mtx1[row][cln]*mtx2[cln][row])
        new_matrix.append(rows)
    print(new_matrix)
mult_matrix(matrix1, matrix2)
