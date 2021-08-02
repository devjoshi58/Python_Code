#Errors and Exception

x=5

if x>5:
    raise Exception("X cannot be greater than 5")




#Using Assert

assert(x>5),'x is not greater than 5'

"""
Traceback (most recent call last):
  File "/Users/varunjoshi/Documents/GitHub/Python_Code/Error_and_exceptions/Assert_and_raise.py", line 11, in <module>
    assert(x>5),'x is not greater than 5'
AssertionError: x is not greater than 5
"""