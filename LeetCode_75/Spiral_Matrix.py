
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2],[3,4]]
matrix= [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#matrix=[[2.3]]
#matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


#00 01 02 12 22 21 20 10 11
left,right = 0, len(matrix[0])-1
top,bottom = 0,len(matrix)-1

res = []

while left<=right and top<=bottom:
    
    #get every value in the top row
    
    for i in range(left,right+1):
        res.append(matrix[top][i])
    top+=1
    
    #get every value of the last column
    
    for i in range(top,bottom+1):
        res.append(matrix[i][right])
    right-=1
    
    
    #get every value in the bottom row
    
    for i in range(right,left-1,-1):
        res.append(matrix[bottom][i])
    bottom-=1
    
    #get every value in left most column
    
    for i in range(bottom,top-1,-1):
        res.append(matrix[i][left])
    left+=1
        
print(res)