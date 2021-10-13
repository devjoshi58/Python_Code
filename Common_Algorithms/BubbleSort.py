#[4,3,2,5,6]
#[3,4,2,5,6]
#[3,2,4,5,6]
#[3,2,4,5,6]
#[2,3,4,5,6]

#complexity O(N*2)

list1 = [4,3,8,2,5,0,6]

for i in range(len(list1)-1,0,-1):
    for j in range(0,i):
        #if  j+1 < len(list1):
        if list1[j]>list1[j+1] :

            a= list1[j]
            print(a)
            list1[j]=list1[j+1]
            list1[j+1]=a


print(list1)
