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
        
        #print(nums)
    
    #place the pivot between

    if j < i:
        nums[j],nums[low]=nums[low],nums[j]
    print(nums)
    return(j)


def quicksort(arr,lower_bound,upper_bound):

    if lower_bound < upper_bound:

        pivot = partition(arr,lower_bound,upper_bound)
        #loc is the pivot hence we call quicksort with pivot -1  and pivot+1
        quicksort(arr,lower_bound,pivot-1)
        #print(arr)
        quicksort(arr,pivot+1,upper_bound)
    
    #print(arr)

#Partition exhange method
nums = [10,7,8,12,15,6,3,9,5]
nums1=[10,7,8,22,23]
quicksort(nums1,0,len(nums1)-1)
#print(nums1)