#Tuple unpacking
#Tuple is immutable and can be efficient working with it especially with large data

mytuple = "Max",23,"Delhi"

name,age,city = mytuple #Tuple unpacking and number of values should match the size of tuple

print(name,age,city)

#Unpacking in given number of parts

mytuple2 = "1","2","3","4","5"

i1,*i2,i3 = mytuple2

print(i1,i2,i3) #result = 1 ['2', '3', '4'] 5
#i2 is returned as a list and it is the middle part

i1,i2,*i3 = mytuple2
print(i1,i2,i3) # 1 2 ['3', '4', '5']


i1,*i2,i3,i4 = mytuple2
print(i1,i2,i3,i4)


