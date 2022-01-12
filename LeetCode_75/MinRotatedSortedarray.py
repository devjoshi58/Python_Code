def minRotatedSortedArray(arr):

    l = 0
    r = len(arr)-1

    #while l<r and len(arr)>1:

    mid = (r+l)//2
    #print(mid)

    if len(arr)==2:
        print(min(arr))
        return

    elif arr[l]>arr[mid]:

        r =mid
    
    elif arr[mid] > arr[r]:

        l=mid
    else:
        print(arr[0])
        return
    #print(arr[l:r+1])
    minRotatedSortedArray(arr[l:r+1])

minRotatedSortedArray([1,2])
minRotatedSortedArray([4,5,6,7,0,1,2])
minRotatedSortedArray([11,13,15,17])
#wac2190086800
#[6,1,2,3,4,5]