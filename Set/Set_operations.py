#Set :unordered,no duplicates,mutable

myset = {1,2,3,4,4}
print(myset)   # {1,2,3,4} no dupes

myset1 = set([1,2,3])
print(myset1) #{1,2,3}

myset2 = set("hello")
print(myset2) # {'l','o','h','e'} in any order

empty_set = set()

#add elements

empty_set.add(1)
empty_set.add(2)
empty_set.add(5)

print(empty_set)

#Remove elements

empty_set.remove(5 )
print(empty_set)

#Remove elements without getting error when the element is not present

empty_set.discard(90) #No error and nothing removed

#Empty the set
empty_set.clear()
empty_set.add(1)
empty_set.add(2)
empty_set.add(5)

#Pop arbitrary number

val = empty_set.pop()

print(val)
print(empty_set)

#Check if element is in the set

if 2 in empty_set:
    print('yes')