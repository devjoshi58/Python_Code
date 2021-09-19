#Unpacking using * operator

def foo(a,b,c):
    print(a,b,c)

mylist = [1,2,3]
mytuple =(1,2,3)
foo(*mylist) #this is like sending each element of the list separately
foo(*mytuple)


def foo(*args):
    result = 0
    for arg in args:
        result = result+arg
    print(result)

mylist1=[1,2,3,4]
mylist2=[2,3,4,5,6]
foo(*mylist1,*mylist2)



