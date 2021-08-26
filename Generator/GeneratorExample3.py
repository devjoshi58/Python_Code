#Memory efficiency comparison

import sys

def firstn(n):
    num = 0
    list1 = []

    while num<n:
        list1.append(num)
        num+=1
    return(list1)

#Using generator

def firstn_generator(n):
    num = 0

    while num<n:
        yield num
        num=num+1

#Both return 45
res= sum(firstn(10))
res2 = sum(firstn_generator(10))

print(sys.getsizeof(firstn(100000))) #800984
print(sys.getsizeof(firstn_generator(10000))) #112 Memory efficient
print(res)
print(res2)