#%, format(),f-string

#First way

var = 'Tom'

mystring = "hey how are you %s"%var
print(mystring)

#Second #f for float and #d for integer

var2 = 3.1234
mystring = "your number is %f" %var2
print(mystring)

#.2 defines number of digits after decimal

var2 = 3.1234
mystring = "your number is %.2f" %var2
print(mystring)


#Third
var2 = 3.1234
mystring = "your number is {}".format(var2)
print(mystring)

var2 = 3.1234
mystring = "your number is {:.2f}".format(var2)  #for two decimal places
print(mystring)


#Newest f string

new_value = f"the variable us {var} and {var2}" #since python 3.6 and is faster

print(new_value)
