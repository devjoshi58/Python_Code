def combinationSum3(k: int, n: int):
        result=[]
        def backtrack(remain,combo,next_start):
            
            if remain==0 and len(combo)==k:
                
                result.append(list(combo))
                return
            
            elif remain<0 or len(combo)==k:
                return
            
            for i in range(next_start,10):
                
                combo.append(i)
                #print(combo)
                backtrack(remain-i,combo,i+1)
                #backtrack
                combo.pop()
        
        backtrack(n,[],1)
        
        return result

print(combinationSum3(3,7))
            
                