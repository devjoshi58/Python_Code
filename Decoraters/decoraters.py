def start_end_decorater(func):

    def wrapper():
        print('start')
        func()
        print("end")

    return wrapper

@start_end_decorater
#Extending the behavior of a function with a decorator
def print_name():
    print('varun')

#print_name = start_end_decorater(print_name) # adding functionality to print_name function

print_name()

#Function with an argument

def start_end_decorater(func):

    def wrapper(*args,**kwargs):
        print('start')
        result = func(*args,**kwargs)
        print("end")
        return result

    return wrapper

@start_end_decorater
#Extending the behavior of a function with a decorator
def add(x):
    return x+10

value = add(5)
print(value)


def dotwice(func):

    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

