class Solution:
    def isValid(self, s: str) -> bool:
        
       
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        
        for char in s:
            
            if char in dict.values():
                stack.append(char)
            elif stack==[] : #For the condition when first bracket is a closed
                return False
            elif dict[char]!=stack.pop():
                return False
            
        return stack==[]