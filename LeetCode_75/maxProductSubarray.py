"""
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""

def maxproductSubarray(arr):

    res = max(arr)
    curmax=1
    curmin=1

    for n in arr:
        if n==0:
            curmax,curmin=1,1
        tmp = curmax*n
        curmax=max(n*curmax,n*curmin,n)
        curmin=min(n*curmax,n*curmin,n)
        res=max(res,curmax)
    
    return(res)

print(maxproductSubarray([2,3,-2,4]))
print(maxproductSubarray([-2,0,-1]))
print(maxproductSubarray([0,2]))
print(maxproductSubarray([-2,3,-4]))
print(maxproductSubarray([-3,0,1,-2]))
