import types
import functools


def decorator_print_name(func):

    @functools.wraps(func)
    def wrapper_print_name(*args,**kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)
    
    return wrapper_print_name

@decorator_print_name
def pass_name(name):
    print(f'The value is {name}')

pass_name('varun')
