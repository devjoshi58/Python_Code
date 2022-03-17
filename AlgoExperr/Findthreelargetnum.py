
array = [1,234,34,67,500]
out = [array[0],array[1],array[2]]
print(min(out))

for i in range(3,len(array)):
		
    if array[i] > min(out):
        index=out.index(min(out))
        out.remove(out[index])
        print(out)
        out.append(array[i])

print(out)