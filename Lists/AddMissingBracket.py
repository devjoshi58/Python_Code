input = "(a)d)r"
input = "()(sdawe"
#input=list(input1.split())
stack=[]
i=0
while i < len(input):

    if input[i]=='(':
        stack.append(input[i])
    
    elif len(stack)!=0 and input[i]==')': 
            stack.pop()
        
    elif len(stack)==0 and input[i]==')':
            print(i)
            input=input[:i]+'('+input[i:]
            print(input)
            i+=1
    
    i+=1

if len(stack)!=0:
    input=input+')'

print(input)
