def sunsetViews(buildings, direction):
    # Write your code here.
	out = []
	
	if direction == 'EAST' and len(buildings)>0:
		#GO FROM THE RIGHT TO LEFT
		out.append(len(buildings)-1)
		max_val = buildings[-1]
		for i in range(len(buildings)-2,-1,-1):
			
			if buildings[i]<= max_val: #max(buildings[i+1:]):
				print(max_value)
				continue
			
			else:
				max_value = buildings[i]
				out.append(i)
		
	elif direction == 'WEST' and len(buildings)>0:	
		out.append(0)
		
		for i in range(1,len(buildings)):
			
			if buildings[i]<=max(buildings[0:i]):
				continue
			
			else:
				out.append(i)
				
	out.sort()	
	return out

print(sunsetViews([3,5,4,4,3,1,3,2],'EAST'))