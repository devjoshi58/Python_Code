from collections import defaultdict
n = int(input())

d=defaultdict(int)

for i in range(0,n):
    word = input()
    d[word]+=1

print(d)