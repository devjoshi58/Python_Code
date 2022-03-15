list_of_indexes = []

array=[1,1,1,1,1]
sequence = [1,1,1]

if len(sequence)> len(array):
    print(False)

if sequence[0] in array:
    list_of_indexes.append(array.index(sequence[0]))

for i in range(1,len(sequence)):

    if sequence[i] in array and sequence[i]!=sequence[i-1]:
        list_of_indexes.append(array.index(sequence[i]))

else:
    print(False)


for j in range(len(list_of_indexes)-1):

    if list_of_indexes[j]>=list_of_indexes[j+1]:
        print(False)

print(True)