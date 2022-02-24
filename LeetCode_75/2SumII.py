nums = [2,7,11,15]
target = 9
l=0
r=len(nums)-1
res=[]

while l<r:

    temp = nums[l]+nums[r]

    if temp>target:
        r=r-1

    elif temp<target:
        l+=1

    else:
        res.append(l)
        res.append(r)
        break

print(res)