#Unpacking using * operator

def foo(a,b,c):
    print(a,b,c)

mylist = [1,2,3]
mytuple =(1,2,3)
foo(*mylist) #this is like sending each element of the list separately
foo(*mytuple)


def foo(*args):
    result = 0
    print(args) #(1, 2, 3, 4, 2, 3, 4, 5, 6)
    for arg in args:
        result = result+arg
    print(result)

mylist1=[1,2,3,4]
mylist2=[2,3,4,5,6]
foo(*mylist1,*mylist2)

#List unpacking

mylist = [1,2,3,4,5]
*beginning,last = mylist
print(beginning) #[1,2,3,4]
print(last) #5

#beg,*middle,*rightmiddle,last = mylist - this is no correct only one unpack operation is allowed

