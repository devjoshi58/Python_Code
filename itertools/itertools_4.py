#groupby

from itertools import groupby

#Function for getting the key

def smaller_than_three(x):
    return x<3

a=[1,2,3,4]
grouped_data  = groupby(a,key=smaller_than_three)
print(grouped_data)

for key,value in grouped_data:
    print(key,list(value)) # value is grouper object we convert it into list

"""
One thing to keep in mind with groupby() is that it isn’t as smart as you might like. 
As groupby() traverses the data, it aggregates elements until an element with a different key is encountered,
at which point it starts a new group:
"""


grouped_data_2 = groupby([1,2,3,4,1,5])
for key,value in grouped_data_2:
    print(key,list(value))

#Third example

data = [{'name': 'Alan', 'age': 34},
        {'name': 'Catherine', 'age': 34},
         {'name': 'Betsy', 'age': 29},
         {'name': 'David', 'age': 33}]

print(data[0]['age'])

grouped_data_3 = groupby(data,lambda x:x['age'])
for key,value in grouped_data_3:
    print(key,list(value))