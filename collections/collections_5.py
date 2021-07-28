#Deque -double ended queue use to remove or add elements from both sides--

from typing import Deque


d = Deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.pop() #remove from the end

print(d)
 
d.popleft() #remove from left
print(d)

d.extend([1,2,3])
print(d)

d.extendleft([8,7,9])

print(d)

d.rotate(1) # shift 1 place to the right

print(d)

d.rotate(-2) #shift 1 place to the left

print(d)