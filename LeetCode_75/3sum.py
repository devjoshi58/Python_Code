nums = [3,0,-2,-1,1,2]
d = {}
value = 0
out = []
for i in range(0,len(nums)):
    x = nums[i]
    curr = nums[:i]+nums[i+1:]
    print(curr)
    for j in range(0,len(curr)):
        

        v = value-curr[j]-x
        #print(j,x,value,v)
        d = {k:v for k,v in enumerate(curr[:j]+curr[j+1:])}
        #print(d)
        if(v in d.values()):
            l = [v,curr[j],x]
            #print(sorted(l))
            if sorted(l) not in out:
                out.append(sorted(l))
    
print(out)

