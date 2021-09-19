#Understanding args and kwargs
#*args means any number of arguments, args is just a name you can use any other name as well
#* is the unpacking operator
#**Kwargs mean any number of positional arguments

def foo(a,b,c=4,*args,**kwargs): #c is default
    print(a,b,c)

    for arg in args: #looping through all the the arguments, here *args is a tuple
        print(arg)
    
    for key,value in kwargs.items(): #**kwargs is a dictionary
        print(key,value)
    

foo(1,2,3,4,5,6,s=4,y=8)

#In this case, you have to bear in mind that order counts. 
#Just as non-default arguments have to precede default arguments, so *args must come before **kwargs.

