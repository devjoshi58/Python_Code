from itertools import groupby
from re import L

l = [1,2,2,2,3,3,4]

#out = [(len(list(c)),int(k)) for k,c in groupby(l)]

for k,c in groupby(l):
    print((int(k),len(list(c))), end = " ")
