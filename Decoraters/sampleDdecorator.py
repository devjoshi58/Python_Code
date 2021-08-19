#Sample Decorator
"""
a decorator is a 
function that takes another function and 
extends the behavior of the latter function without explicitly modifying it.
"""
def mydecorator(func):

    def wrapper():
        #do somthing
        func()
        #do something
    return wrapper

@mydecorator
def print_name():
    print('name')

print_name()