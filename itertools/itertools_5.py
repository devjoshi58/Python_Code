#Infinite Iterators

from itertools import count,repeat,cycle

for i in count(10): #cycles infinitely
    print(i)
    if i == 20: #Breaks here after the condition otherwise count function would produce an infinite loop
        break

a = [1,2,3,4,5]

for i in cycle(a):
    print(i) #Cycles through infinitely
    if i == 3:
        break

for j in repeat(1,4): #This means repeat 1, 4 times
    print(j)