count = 0
s='aaa'
for i in range(len(s)):
    
    l,r = i,i
    
    while l>=0 and r<len(s) and s[l]==s[r]:
        count+=1
        print(s[l:r+1])
        l-=1
        r+=1
        
    
    l,r=i,i+1
    while l>=0 and r<len(s) and s[l]==s[r]:
        count+=1
        print(s[l:r+1])
        l-=1
        r+=1
        

print(count)