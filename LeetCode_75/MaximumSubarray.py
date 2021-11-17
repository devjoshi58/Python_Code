#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.


def maxsubarray(arr):

    cursum = 0
    maxsub = arr[0]

    for n in arr:
        if cursum<0:
            cursum = 0
        
        cursum = cursum+n
        maxsub = max(cursum,maxsub)
    
    print(maxsub)

maxsubarray([-2,1,-3,4,-1,2,1,-5,4])

maxsubarray([5,4,-1,7,8])

nums=   [-2,1,-3,4,-1,2,1,-5,4]    
for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
            print(nums)
print (max(nums))

