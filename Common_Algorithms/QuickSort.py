def partition(nums,low,high):

    pivot = nums[low]
    i=low
    j=high

    while i<=j:

        if nums[i]<=pivot:
            i+=1
        
        elif nums[j]>pivot:
            j-=1
        
        else:

            nums[i],nums[j] = nums[j],nums[i]
        
        print(nums)
    
    #place the pivot between

    if j < i:
        nums[j],nums[low]=nums[low],nums[j]

    print(nums)
nums = [10,7,8,12,15,6,3,9,5]

partition(nums,0,len(nums)-1)