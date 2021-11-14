def sumofTwo(nums,target):

    d={}

    for i,x in enumerate(nums):
        nbr = target-x
        if nbr in d.keys():
            return(d[nbr],i)
        d[x]=i


result = sumofTwo([2,7,11,15],9)
print(result)
result = sumofTwo([3,2,4],6)
print(result)

result = sumofTwo([3,3],6)
print(result)

