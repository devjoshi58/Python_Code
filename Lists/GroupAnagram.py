strs = ["eat","tea","tan","ate","nat","bat"]

from collections import defaultdict

dict1=defaultdict(list)
dict2 = {}

for i in strs:
    s="".join(sorted(i))
    dict1[s].append(i)

print([i for i in dict1.values()])