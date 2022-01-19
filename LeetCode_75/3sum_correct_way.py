def threesum(nums):

    #nums=[-1,1]
    res = []
    nums.sort(reverse=True)

    l=0
    r=len(nums)-1

    if len(nums)<3:
        print(nums)
        return nums
    
    for i in range(0,len(nums)): #fixing one out of three to form triplets that have sum =0

        if len(nums)<=0:
            break

        elif i>0 and nums[i]==nums[i-1]:

            continue
        
        else:
            l=i+1
            r=len(nums)-1

            while l<r:
                temp = nums[i]+nums[l]+nums[r]
                if temp == 0:

                    res.append([nums[i],nums[l],nums[r]])
                    while(l<r and nums[l]==nums[l+1]):
                        l=l+1
                    
                    while(l<r and nums[r]==nums[r-1]):
                        r=r-1
                    l=l+1
                    r=r-1
                elif temp>0: # as the nums is in desc order move to right to go near zero
                    l=l+1
                
                elif temp<0:
                    r=r-1

    print(res)


threesum([0])         

