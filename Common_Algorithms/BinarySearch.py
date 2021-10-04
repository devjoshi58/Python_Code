def binarySearch(list_of_numbers,num):

    lo = 0
    hi = len(list_of_numbers)-1
    
    while lo<=hi:
        mid = (hi+lo)//2
        print(f'mid: {mid} hi: {hi} lo: {lo}')
        if num == list_of_numbers[mid]:
            print(f"found {num} at {mid}")
            return num
        
        elif num>list_of_numbers[mid]:
            hi = mid -1
        
        elif num<list_of_numbers[mid]:
            lo = mid+1
    
    return -1

def evaluateTests(list_of_tests,func_name):

    for test in list_of_tests:
        func_name(test["numlist"],test["num"])


if __name__ == "__main__":

    inputs = [{"numlist":[8,7,6,4,3,2],"num":7},
    {"numlist":[8,7,6,4,3,2],"num":3},
    {"numlist":[8,7,6,6,6,2,9],"num":6}]
    
    evaluateTests(inputs,binarySearch)
    #binarySearch(inputs[0]["numlist"],inputs[0]["num"])
