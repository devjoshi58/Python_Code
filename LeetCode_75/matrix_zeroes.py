from token import RARROW


matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

r=[]
c=[]

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col]==0:
            r.append(row)
            c.append(col)


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i in r or j in c:
            matrix[i][j]=0

print(matrix)


