import functools

def dotwice(func):

    def wrapper_do_twice(*args,**kwargs):
        print("wrapper do twice")
        res = func(*args,**kwargs)
        return res
        #func(*args,**kwargs)
    return wrapper_do_twice

def add(func):
    def wrapper_add(*args,**kwargs):
        print("wrapper add")
        result = func(*args,**kwargs)
        return(result)
    
    return(wrapper_add)



@dotwice
@add
def test_f(x):
    print('test called')
    return x+5

value = test_f(5)
print(value)
