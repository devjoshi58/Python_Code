#Try and except

a=10
print(a)
try:
    x=a-'t' #if this fails then type error, replace 0 with str
    y= 5/4 # this fails with division by zero error

except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("ALL WELL NO EXCEPTIONS")
finally:
    print("will run always and can be used for clean up operations")