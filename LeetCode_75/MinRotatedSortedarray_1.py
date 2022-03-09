#arr=[1,2]
arr=[4,5,6,7,0,1,2]
arr=[11,13,15,17]

l=0
r=len(arr)-1

if arr[0]<arr[r]:
    print(arr[0])
    exit

while l<=r:
    mid = l+(r-l)//2
    #print(arr[mid])

    if len(arr[l:r+1])<=2:
        print(min(arr))
        break


    elif arr[mid]>arr[r]:
        l=mid

    elif arr[mid]<=arr[l]:
        r=mid
    