#Set unordered mutable and no dups

a = {1,2,3,4,5}
b = {1,2,3,4,5,6,7}

#check if a is subset of b

print(a.issubset(b))

#superset check

print(a.issuperset(b))

#disjoint for false case

print(a.isdisjoint(b))

#disjoint check for true case 

a={12,3,33}
b={4,5}
print(a.isdisjoint(b))

#Frozen set - immutable version of a normal set
#UNION INTERSECTION WILL WORK

a= frozenset([1,2,3,4])

#a.add(5) # Error
#a.remove(4) #Error