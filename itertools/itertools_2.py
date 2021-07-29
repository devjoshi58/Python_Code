#itertools: product,permutations,combinations,accumulate,groupby and infinite iterators

from itertools import permutations

a = [1,2,3]

perm1 = permutations(a)

print(list(perm1))
#[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
#Returns all possible permutations

#Different length of permutations

perm1 = permutations(a,2)
print(list(perm1))
#[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

from itertools import combinations,combinations_with_replacement

b = [1,2,3]

comb1 = combinations(b,2)
print(list(comb1))

#[(1, 2), (1, 3), (2, 3)]]

comb2 = combinations_with_replacement(b,2)
print(list(comb2))
#[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]]
#Same element is paired as well