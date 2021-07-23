#List operations
#List ordered mutable and can contain duplicates

mylist= ['apple','banana','mango','orange']

#Add element at the end
mylist.append('watermelon')

print(mylist)
# inserting at a particular index position
mylist.insert(0,'peach') 
print(mylist)

#sort it in place
mylist.sort()
print(mylist)

new_list =[0]*5
print(new_list)

#combine two list

combined_list = mylist+new_list
print(combined_list)

#slicing mylist[start:stop:step]

print(mylist[:4])

#copy list

list_org = ['cherry','apple','banana']
list_copy = list_org

list_copy.append("lemon")
print(list_copy)
print(list_org)

#Here both list get updated as they both point to same list in the memory
#So copy we need

list_copy = list_org.copy()
print(list_copy)

list_copy.append('creek')
print(list_copy) #no only list copy gets appended 