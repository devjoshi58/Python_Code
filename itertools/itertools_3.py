#itertools: product,permutations,combinations,accumulate,groupby and infinite iterators

from itertools import accumulate

a=[4,1,2,3,4,7]

acc = accumulate(a) #By default the operator here is sum
print(list(acc))
#[4, 5, 7, 10, 14, 21]


#To use any other operator other than default sum

import operator

acc_multiply = accumulate(a,operator.mul)
print(list(acc_multiply))

#Getting max number
acc_max = accumulate(a,func=max)
print(list(acc_max))

