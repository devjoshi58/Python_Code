#Counters,defaultdict,deque,namedtuple,ordereddict

from collections import Counter

mystring = 'aaaarrffttyy'

my_counter = Counter(mystring)

print(my_counter)
print(type(my_counter))
print(my_counter.items())
print(my_counter.keys())

#To get the key with most count

print(my_counter.most_common(1))
#TO get top 2

print(my_counter.most_common(2))

#Get the key with most count

print(my_counter.most_common(1)[0][0])  

# To put all the repeated elements one by one in a list

new_list = list(my_counter.elements()) # "aaddff" to [a,a,d,d,f,f]
print(new_list)

