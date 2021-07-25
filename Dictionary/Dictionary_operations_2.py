#Dictionary operations

mydict2 = dict(name="max",age=27,city='delhi')

mydict_copy = mydict2.copy()

print(mydict_copy)

mydict_copy["new_element"] = "test"

print(mydict_copy)

#Merge two dictionaries with update method

mydict1 = dict(name="max",age=27,city='delhi')
mydict3 = {"name":"yoo","age":34,"state":"UT"}

mydict1.update(mydict3) #mydict1 gets updated for the common keys and different keys remain as is
print(mydict1)

#Merge test

mydict1 = dict(name="max",age=27,city='delhi')
mydict3 = {"name":"yoo","age":34,"state":"UT"}

mydict3.update(mydict1)
print(mydict3)
  
#Any immutable type can be used as keys such as tuple,integer,string

mytuple = 1,2
print(type(mytuple))

mydict4 = {mytuple:3 }
print(mydict4)

#list cannot be used as keys as they are mutable hence hashable