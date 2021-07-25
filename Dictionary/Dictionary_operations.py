#Dictionary key value pair, unordered, mutable

mydict = {"name":"max","Age":29,"city":"delhi"}

#another way to create a dictionary

mydict2 = dict(name="max",age=27,city='delhi')


#ADD ITEMS

mydict2["email"]='hr@youtube.com'

print(mydict2)

#Delete element

del mydict2["age"]
print(mydict2)

#delete element way -2

mydict2.pop("city")

print(mydict2)

#delete last item in the dictionary  

mydict2.popitem()
print(mydict2)

#Loop through dictionary
mydict2 = dict(name="max",age=27,city='delhi')
for key in mydict2.keys():
    print(key)

#loop through values

for val in mydict2.values():
    print(val)

#to get both key and value

for key,value in mydict2.items():
    print(key,value)

for i in mydict2.items():
    print(i) #tuple
    print(i[0],i[1])

