# Write your code here.
array = [1,2,3,4,5,6,7,8]
target = 5
left = 0
right = len(array)-1
mid=(right+left)//2

while left<right:
    
    if array[mid]==target:
        print(mid)
        break

    mid = (right+left)//2
    print(mid)
    
    
    
    if array[mid]>target:
        right=mid-1
    
    else:
        left=mid

