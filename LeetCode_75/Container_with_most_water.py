class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        start=0
        end = len(height)-1
        final=0

        while start<end:
            
            area = min(height[start],height[end]) * (end-start)
            final = max(final,area)
            
            if height[start]<=height[end]:
                start+=1
            
            else:
                end-=1
        
        return(final)