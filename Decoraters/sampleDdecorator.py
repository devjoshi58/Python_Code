#Sample Decorator

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