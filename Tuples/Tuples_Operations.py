#tuples: Ordered immutable and allows duplicate element

mytuple = ("Max",) #if no comma then its a string

#Creating tuple from a list

mytuple1 = tuple(['Max',28,"Male"])
item = mytuple1[0]

print(item)

#iterating over tuple

for i in mytuple1:
    print(i)

#check if an element is inside tuple

if 'max' in mytuple1:
    print("Yes")

#length of tuple

print(len(mytuple1))

new_tuple = ('a','a','p','y','i')
print(new_tuple.count('a'))

#find index

print(new_tuple.index('y'))

#Value error if we try to find index of a non existing element

##new_tuple.index('r') 

#convert to a list and vice versa

mylist = list(new_tuple)
print(mylist)

mytuple2= tuple(mylist)
print(mytuple2)

#slicing

print(mytuple2[1:3])
print(mytuple2[::-1]) #reverse

