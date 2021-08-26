def febonacci_With_generator(limit):
    a=0
    b=1

    while a < limit:
        yield a
        a,b = b,a+b
        

febo = febonacci_With_generator(10)

for i in febo:
    print(i)



