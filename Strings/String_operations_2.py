#Other operations

mystring = "Hello Varun"

print(mystring.startswith('hello')) #False

print(mystring.startswith('Hello')) #True

print(mystring.endswith("un"))

print(mystring.lower())

#Find index of a character

print(mystring.find('H'))

print(mystring.find('HEL'))

print(mystring.find('Z')) #-1

#Count a particular character

print(mystring.count('l')) #2

#Replace 

new_string = mystring.replace('Hello','Bye')
print(new_string)
print(mystring)

#Convert string to list

list_from_string= new_string.split(" ")
print(list_from_string)

#List to back to string

new_string1 = ' '.join(list_from_string)
print(new_string1)

