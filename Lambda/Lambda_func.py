#lambda argument : expression

add10 = lambda x: x+10
print(add10(5))

#above is same as below

def add_10(x):
    print(x+10)

add_10(5)

#Lambda with multiple arguments

mult = lambda x,y: x*y
print(mult(2,4))

#Lambda is used with higher order functions
#Higher order functions are function that another function as argument
# Example sorted,map,filter,reduce

#First Sorted Method

points_2d = [(1,2),(4,5),(6,9),(0,2)]
points_2d_sorted = sorted(points_2d)
print(points_2d_sorted)

#Sort by second value in a tuple

points_2d_sorted_by_2nd = sorted(points_2d,key= lambda x:x[1])
print(points_2d_sorted_by_2nd)

#Sort by sum of each tuple

points_2d_sorted_by_sum = sorted(points_2d,key= lambda x:x[1]+x[0],reverse=True)
print(points_2d_sorted_by_sum)