#class decorator

import functools

class Countcalls:

    def __init__(self,func):
        self.func = func
        self.num_counts = 0
    
    def __call__(self,*args,**kwargs):  #similaar to the wrapper function in other decorators
        self.num_counts+=1
        print(f"{self.num_counts} of function {self.func.__name__}")
        self.func(*args,**kwargs)

@Countcalls
def say_whee():
    print("whee")

say_whee()
say_whee()
print(say_whee.num_counts)