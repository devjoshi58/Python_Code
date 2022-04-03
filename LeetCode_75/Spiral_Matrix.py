
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2],[3,4]]
matrix= [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix= [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
  ]
#matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#matrix=[[2.3]]
#matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


#00 01 02 12 22 21 20 10 11
def spiralTraverse(array):
    # Write your code here.
	startRow = 0
	endRow = len(array)
	startCol = 0
	endCol = len(array[0])
	out=[]
	while startRow<endRow and startCol<endCol:
		
		for i in range(startCol,endCol):
			out.append(array[startRow][i])
		
		startRow+=1
		
		for i in range(startRow,endRow):
			out.append(array[i][endCol-1])
			i+=1
		
		endCol-=1
		#to tackle when single row is left
		if not(startRow<endRow and startCol<endCol):
	        break
		
		for i in range(endCol-1,startCol-1,-1):
			out.append(array[endRow-1][i])

		endRow-=1
		
		for i in range(endRow-1,startRow-1,-1):
			out.append(array[i][startCol])
			
		startCol+=1
	
	return out
	
	
    pass
