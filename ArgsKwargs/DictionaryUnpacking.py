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

mydict2= {1:'a',2:'b',3:'c'}
*key1,lastkey = mydict2
print(key1) #list of keys
print(lastkey)