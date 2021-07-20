#Program to perform merge sort of two lists
#Time Complexity : O(n1 + n2) 
#Auxiliary Space : O(n1 + n2)
#https://www.geeksforgeeks.org/merge-two-sorted-arrays/


def merge_two_sorted_list(arr1,arr2):

    merged_list = []

    #if len(arr1)>len(arr2):
    #    merge_Sort(arr2,arr1)
    
    i=j=0

    while i<len(arr1) and j<len(arr2):

        if arr1[i]>arr2[j]:
            merged_list.append(arr2[j])
            j=j+1
        
        elif arr1[i]<=arr2[j]:
            merged_list.append(arr1[i])
            i=i+1

    
    while i<len(arr1):
        merged_list.append(arr1[i])
        i=i+1
    
    while j<len(arr2):
        merged_list.append(arr2[j])
        j+=1
    
    print(merged_list)

if __name__ == '__main__':

    arr1= [1,2,6,8,9,10]
    arr2= [2,4,7,8]
    merge_two_sorted_list(arr1,arr2)

#result - [1, 2, 2, 4, 6, 7, 8, 8, 9, 10]

        
