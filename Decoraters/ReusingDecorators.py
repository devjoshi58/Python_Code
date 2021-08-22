from decoraters import dotwice

@dotwice
def print_whee():
    print("whee")

print_whee()

print(print_whee) # the function now thinks it is the wrapper_do_twice function inside the decorator 
#To fix this, decorators should use the @functools.wraps decorator, 
# which will preserve information about the original function. 
#check functools.py