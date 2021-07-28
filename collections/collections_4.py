#Counters,defaultdict,deque,namedtuple,ordereddict

from collections import defaultdict

mydict = defaultdict(int) # default type has to be given for the value

mydict['a']=1
mydict['b']=2
print(mydict['a'])
print(mydict['c']) #prints default value 0 as we have int as default type


#Using list as default type

mydict2 = defaultdict(list)

mydict2[1]=['a','b']
print(mydict2[1])
print(mydict2[4]) #Prints empty list

