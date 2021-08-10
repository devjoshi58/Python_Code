import random

a = random.randrange(0,15)
print(a)

b = random.normalvariate(0,1) #Random value from normal distribution

print(b)

mylist = list('12345')
b= random.choice(mylist)
print(b)

 #Pick multiple random elements from list

c = random.sample(mylist,2) #picks unique element only
print(c)

#Shuffle method

random.shuffle(mylist)
print(mylist)