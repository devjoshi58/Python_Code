string = 'abc'
key =52 

res = ""
for i in string:
    
    if ord(i)+key>122:
        curr = ord(i)+key -122
        res+=chr(96+curr)
    
    if ord(i)+key<=122:
        res+=chr(ord(i)+key)

print(res)

print(1000%26)
