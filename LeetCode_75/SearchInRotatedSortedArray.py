"""
def SearchinRotatedArray(nums,target):

    dict = {}
        
    for i,j in enumerate(nums):
            
        dict[j]=i
        
    print(dict)

    print(dict[target])
"""

nums = [4,5,6,7,0,1,2]

#SearchinRotatedArray(nums,9)

#Below solution using binary search

def UsingBinarySearch(nums,target):

    start = 0
    end = len(nums)-1

    while start<=end:

        mid = (end+start)//2
        
        if nums[mid]==target:
            print(mid)
            return

        elif nums[start] <= nums[mid]:#check if left side of the mid is sorted
            if target>=nums[start] and target<nums[mid]:
                end = mid-1
            else:
                start = mid+1
        
        elif nums[mid]<nums[end]: #check if right side of the mid is sorted
            if target > nums[mid] and target <= nums[end]:
                start = mid+1
            else:
                end = mid-1
    
    print(-1)
    return
nums2 =  [4,5,6,7,0,1,2]
UsingBinarySearch(nums2,56)