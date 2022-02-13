#lambda argument : expression

list1 = [1,2,3,4,5,6]
#map(func,seq)
map_output = map(lambda x:x*2,list1)
print(list(map_output))


#Using Filter

filter_output = filter(lambda x:x%2==0,list1)
print(list(filter_output))
#filtero = filter(lambda x:x%2==0,list1
# )
#Both can be done by list comprehension as well which is a better way

#Reduce function
#reduce(func,seq)

#using min
min_output = min(list1)
print(min_output)


from functools import reduce


"""
Apply a function of two arguments cumulatively to the items of a sequence, from left to right,
 so as to reduce the sequence to a single value.
"""
reduce_result = reduce(lambda x,y:x+y,list1) #Reduce takes 2 arguments
print(reduce_result)


high_ordeR_func = lambda x,func:x+func(x)
print(high_ordeR_func(2,lambda x:x+1))