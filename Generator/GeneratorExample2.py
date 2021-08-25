def countdown(num):
    print('starting')
    while num>0:
        yield num
        num-=1

cd = countdown(5)
print(type(cd))

#print(next(cd))

for i in countdown(5):
    print(i)
    