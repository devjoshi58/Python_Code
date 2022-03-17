# Write your code here.
string = 'AAAAAAAAAAAABBCCCCDD'
string=string+str(1)
out = ""
count=1
for index in range(0,len(string)-1):
    
    if string[index]==string[index+1] and count!=9:
        count+=1
        continue
    
    else:
        
        out=out+str(count)+str(string[index])
        count=1

print(out)