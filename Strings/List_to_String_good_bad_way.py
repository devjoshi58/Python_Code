from timeit import default_timer as timer

mylist = ['w']*1000000

#Bad way to convert list to string
mystring = ""
start = timer()
for i in mylist:
    mystring+=i

stop = timer()
print(stop-start)
#print(mystring)


#Right way is to use join-- this is much faster

start = timer()
mystring = ''.join(mylist)
stop = timer()
print(stop-start)