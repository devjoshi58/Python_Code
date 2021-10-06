#First and Last position of a number using binary search

def firstPosition(num_list,num):

    hi = len(num_list)-1
    lo = 0

    while lo<=hi:
        mid= (hi+lo)//2
        
        if num == num_list[mid]:
            
            while num==num_list[mid-1] and mid>0:
                mid=mid-1
            print("found first position")
            print(mid)
            return mid
        
        elif num<num_list[mid]:
            hi=mid-1
        
        elif num>num_list[mid]:
            lo=mid+1
    
    return -1

def LastPosition(num_list,num):

    hi = len(num_list)-1
    lo = 0

    while lo<=hi:
        mid= (hi+lo)//2
        
        if num == num_list[mid]:
            
            while num==num_list[mid+1] and mid>0:
                mid=mid+1
            print("found last position")
            print(mid)
            return mid
        
        elif num<num_list[mid]:
            hi=mid-1
        
        elif num>num_list[mid]:
            lo=mid+1
    
    return -1

def evaluateTests(list_of_tests,func_name1,func_name2):

    for test in list_of_tests:
        func_name1(test["numlist"],test["num"])
        func_name2(test["numlist"],test["num"])


if __name__ == "__main__":

    inputs = [{"numlist":[1,2,3,4,5,6,7,7,7,8],"num":7},
    {"numlist":[1,2,3,4,5,6,7],"num":3},
    {"numlist":[6,6,6,7,8,9],"num":6},
    {"numlist":[4,5,6,7,8,9],"num":6}]
    
    evaluateTests(inputs,firstPosition,LastPosition)
    #binarySearch(inputs[0]["numlist"],inputs[0]["num"])   