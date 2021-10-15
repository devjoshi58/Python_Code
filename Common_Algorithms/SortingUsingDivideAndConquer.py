#Merge Sort

def sort(list_nums):

    if len(list_nums)<=1:
        return list_nums

    mid = len(list_nums)//2

    left = list_nums[:mid]
    right = list_nums[mid:]


    left_sorted, right_sorted = sort(left),sort(right)
    
    #print(left_sorted)
    #print(right_sorted)
    sorted_num = merge(left_sorted,right_sorted)
    print(sorted_num)
    
    return(sorted_num)

def merge(left_num,right_num):

    new_list = []

    #if len(left_num)>len(right_num):
    #    right_num,left_num = left_num,right_num
    
    i=j=0

    while i < len(right_num) and j< len(left_num):

        if left_num[j]<=right_num[i]:
            new_list.append(left_num[j])
            j+=1
        
        else:
            new_list.append(right_num[i])
            i+=1
    #print(new_list)

    return(new_list + left_num[j:]+right_num[i:])

print(sort([2,4,5,9,1]))