#Set: unordered,mutable,no dups

even = {0,2,4,6,8}
odd = {1,3,5,7,9,9}
prime ={2,3,5,7}

#Combine two sets without duplication

u = even.union(odd)
print(u)

#Intersection

i = odd.intersection(even)
print(i) #empty

#Intersection 2

i2 = even.intersection(prime)
print(i2)

#Difference of two sets
a = {1,2,3,4,5,6,7,8,9}
b = {1,2,3,11,12,13}

res = a.difference(b) # returns elements from a which are not in b - 4,5,6,7,8,9 
print(res)

#Symmettric difference

res2 = a.symmetric_difference(b)
print(res2) #returns elements that are not in both sets 

#update set

a.update(b) #updates the set 1 in place with elements from b without duplication
print(a)

#intersection update method
 
a.intersection_update(b) # a will have elements that exist in both sets
print("after intersection update",a) 

#difference update

a.difference_update(b)
print(a) # elements of a that are not in b

#symmetric difference

a.add(0)
a.symmetric_difference(b)
print(a)