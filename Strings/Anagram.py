s='anagram'
t='nagrama'


from collections import Counter

dict1 = Counter(s)
dict2 = Counter(t)

print(dict1)
print(dict2)

for i in s:

    if dict1[i]!=dict2[i]:
        print('False')
    

print('True')
