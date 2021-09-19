def foo(a,b,c):
    print(a,b,c)

mydict1 = {'a':1,'b':2,'c':3} #the key names should be same as the parameters in function,we can use kwargs as well 
#then no rule one same name.
foo(**mydict1)


def dictunpack(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

mydict1 = {'a':1,'b':2,'c':3} 

dictunpack(**mydict1)