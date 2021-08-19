from datetime import datetime

def decorator_time_check(func):
    def wrapper():
        print(datetime.now().hour)
        if 7< datetime.now().hour<24:
            print("wheeeeeee")
        else:
            pass
        func()
    
    return wrapper # returning the reference to the function, not evaluating the function

@decorator_time_check # say_whee now points to wrapper() inner function,Remember that you return wrapper as a function 
def say_whee():
    print("whee")

#say_whee = decorator_time_check(say_whee) --this is another way of using the decorator
print(say_whee) #Wrapper reference is returned

say_whee() #calling the function
