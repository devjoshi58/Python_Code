mylist1 = [1,2,3]

mylist2 = [4,5,6]

merged_list = [*mylist1,*mylist2]
print(merged_list)


#merge tuple and list into list

mylist1 = (1,2,3)

mylist2 = [4,5,6]

merged_list = [*mylist1,*mylist2]
print(merged_list)

#merge set and tuple

mylist1 = (1,2,3)

mylist2 = {4,5,6}

merged_list = [*mylist1,*mylist2]
print(merged_list)

#merge dictionary

dict1 = {1:'a',2:'c',3:'r'}
dict2 = {3:'d',4:'y'}

mergeddict = {**dict1,**dict2}
print(mergeddict)