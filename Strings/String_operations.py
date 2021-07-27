#String :Immutable,ordered,text representation

mystring = "hello"
print(mystring)
mystring1 = "'hello'"
print(mystring1)

#multi line string

multi_line_String = """hey
                    whats up--multi line"""

print(multi_line_String)

 #Access characters

mystring = "varun joshi"
print(mystring[-1]) #last character

#We cannot access a character and change it as string is immutable

substring = mystring[1:5]
print(substring)

#reverse the string

print(mystring[::-1])

#print every second character

print(mystring[::2])

#string concatenation

concat = mystring+mystring1
print(concat)

#loop over string

for i in concat:
    print(i)

#Remove wide spaces from the string

test_string = '  Hello bro  '
new_string = test_string.strip()
print(new_string)
 

