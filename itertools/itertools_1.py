#itertools: product,permutations,combinations,accumulate,groupby and infinite iterators
"""
What Is Itertools and Why Should You Use It?
According to the itertools docs, it is a “module [that] implements a number of iterator building blocks 
inspired by constructs from APL, Haskell, and SML… Together, they form an ‘iterator algebra’ making it 
possible to construct specialized tools succinctly and efficiently in pure Python.”

Loosely speaking, this means that the functions in itertools “operate” on iterators to produce 
more complex iterators. Consider, for example, the built-in zip() function, which takes any number of 
iterables as arguments and returns an iterator over tuples of their corresponding elements:

"""

from itertools import product

#This will create a cartesian product

list1 = [1,2]
list2 = [3]

prod = product(list1,list2)

print(list(prod))
#[(1, 3), (1, 4), (2, 3), (2, 4)]

#Product with repeat

prod2 = product(list1,list2,repeat=2)
print(list(prod2))
