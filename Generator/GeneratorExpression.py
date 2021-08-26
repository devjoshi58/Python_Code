import sys

mygenerator = (i for i in range(10000) if i%2 ==0)

#for i in mygenerator:
   #print(i)

print(sys.getsizeof(mygenerator)) #112

mylist = [i for i in range(10000) if i%2==0]

print(sys.getsizeof(mylist)) #41880

