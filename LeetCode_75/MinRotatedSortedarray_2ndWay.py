class Solution(object):
    def findMin(self, nums):

        if len(nums)==1:
            return nums[0]
        
        left = 0
        right = len(nums)-1
        

        #If last value is greater than first then array is sorted hence first value is smallest

        if nums[0]< nums[right]:
            return nums[0]
        
        while right > left:

            mid = (left+right)//2
        #If mid-1 is > mid then mid is the infliction point

            if nums[mid-1] > nums[mid]:
                return(mid)
            
            #if mid+1 is less than mid

            elif nums[mid+1] < nums[mid]:
                return(mid+1)
            

            elif nums[mid]>nums[left]:
                left = mid+1
            
            else:
                right = mid-1

s = Solution()
print(s.findMin([5,6,1,2,3,4]))
            