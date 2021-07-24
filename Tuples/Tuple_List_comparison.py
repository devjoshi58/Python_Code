#Tuple is immutable and can be efficient working with it especially with large data

import sys

mylist = [1,2,3,'Hello','True']
mytuple = (1,2,3,'Hello','True')

#same elements but tuples takes less space
print(sys.getsizeof(mylist),'bytes') #120 bytes
print(sys.getsizeof(mytuple),'bytes') #80 bytes

#Comapring time taken to create list and tuple a million times
#Working with tuples can be more efficient than lists

import timeit

print(timeit.timeit(stmt="[1,2,3,4,5]",number=1000000)) #0.044351955
print(timeit.timeit(stmt="(1,2,3,4,5)",number=1000000)) #0.0054033939999999-- tuple takes less time