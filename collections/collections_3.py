#Counters,defaultdict,deque,namedtuple,ordereddict
#After 3.6 dictionary is ordered by default --

from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict[0]=1
ordered_dict[1]=2
ordered_dict[3]=4

print(ordered_dict)

mydict = dict()
mydict[0]=1
mydict[1]=2
mydict[2]=3

print(mydict) # this is also ordered as this is python 3.6