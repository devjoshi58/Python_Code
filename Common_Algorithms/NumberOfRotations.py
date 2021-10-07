#[1,2,3,4,5,6,7,8,9]
#[9,1,2,3,4,5,6,7,8]
#[2,3,4,7,8,9,1] when mid element is greater than the last element then move to right
#[8,1,2,3,4,5,6 ] when mid element is less than the last element then move to left

def NumberofRotations(num_list):

    hi = len(num_list)-1
    lo = 0

    while lo<=hi:

        mid = (hi+lo)//2

        if num_list[mid]< num_list[mid-1]:
            print(f"rotations = {mid}")
            return
        
        elif num_list[mid] < num_list[hi]:
            hi=mid-1
        
        elif num_list[mid]>num_list[hi]:
            lo=mid+1
    
    return 0

def evaluateTests(list_of_tests,func_name):

    for test in list_of_tests:
        func_name(test["numlist"])


if __name__ == "__main__":

    inputs = [{"numlist":[5,6,7,1,2,3,4]},
    {"numlist":[3,4,1,2]}]
    
    evaluateTests(inputs,NumberofRotations)
    #binarySearch(inputs[0]["numlist"],inputs[0]["num"])
        