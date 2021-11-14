#Input: nums = [1,2,3,4]
#Output: [24,12,8,6]

#Input: nums = [-1,1,0,-3,3]
#Output: [0,0,9,0,0]

#[0,1,2,6]
#[24,12,4,0]

nums = [-1,1,0,-3,3]
left = [1]
right =[1]
#first pass from the left
p=1


for i in range(1,len(nums)):
    p=p*nums[i-1]
    left.append(p)

print(left)

#second pass from the right
p=1

for j in range(len(nums)-2,-1,-1):
    p=p*nums[j+1]
    right.append(p)
    #print(right)
right = right[::-1]

print(right)
final = []
for i in range(0,len(right)):
    final.append(left[i]*right[i])

print(final)