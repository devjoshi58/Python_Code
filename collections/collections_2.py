#Counters,defaultdict,deque,namedtuple,ordereddict

"""
Python’s namedtuple() is a factory function available in collections.
 It allows you to create tuple subclasses with named fields. 
 You can access the values in a given named tuple using the dot notation and the field names, 
like in obj.attr.
Python’s namedtuple was created to improve code readability by providing a way to access values using
 descriptive field names instead of integer indices, which most of the time don’t provide any
  context on what the values are. This feature also makes the code cleaner and more maintainable.
"""

from collections import namedtuple

#Pythonic way of using the tuple, we are able to access the elements with a name rather than index
point = namedtuple("point","x,y")
pt = point(1,2)

print(pt.x,pt.y)
hash(pt)

#tuples are immutable but they can have mutable values like below

person = namedtuple('person','name,children')
john = person('john',['child1','child2'])

print(john.name)
print(john.children)

john.children.append('child3') #Mutable element in tuple

#hash(john) not hashable as it has mutable element inside.
#Should use a data structure that is ordered only like here we use list and not set.

print(john)