from itertools import groupby

result = "1"
v=''
n=8

for _ in range(n-1):
    v=''
    for digit,group in groupby(result):
        print(type(group))
        count=len(list(group))
        print('count',len(list(group)))
        v += "%i%s" % (count, digit) # create the 21 string and accumulate it
        print(f'v={v}')
    result = v # save to result for the next for loop pass

print(v)
