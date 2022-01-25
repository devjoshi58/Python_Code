"""Given a two dimensional list, for example [ [2,3],[3,4],[5]] person 2 is 
friends with 3 etc, find how many friends each person has. 
Note, one person has no friends"""

from collections import defaultdict


l = [[2,3],[3,4],[5]]

dict = defaultdict(int)

for i in l:

    for j in range(0,len(i)):

        if i [j] in dict.keys():

            dict[i[j]]+=1
        
        else:
            dict[i[j]]=1

print(dict)


"""Complete a function that returns a list containing all the mismatched words (case sensitive) 
between two given input strings # For example: # - string 1 : "Firstly this is the first string" #
 - string 2 : "Next is the second string" # # - output : ['Firstly', 'this', 'first', 'Next', 'second']"""

s1 = "Firstly this is the first string"
s2 = "Next is the second string"

list1 = s1.split(" ")
list2 = s2.split(" ")
print(list1)
print(list2)

out = list(set(list1)-set(list2)) + list(set(list2)-set(list1))

print(out)
