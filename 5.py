matrix1= [[1,2,3],
         [6,7,8]]

matrix2= [[6,1],
         [2,10],
         [0,2]]
new_matrix= [[0,0],
              [0,0]]
#def mult_matrix(mtx1,mtx2):

for row in range(len(mtx1)):
        rows=[]
        for cln in range(len(mtx2)):
           rows=(mtx1[row][cln]*mtx2[cln][row])
           for n in range(len(new_matrix)):
               n = row *cln
           #for row in range (len(mtx1)):
print(n)