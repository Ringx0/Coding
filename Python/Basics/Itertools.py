from itertools import product

# Cartesian product of two lists
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(prod)  # Prints a product object
print(list(prod))  # Converts the product object to a list

# Cartesian product with repeat
prod = product(a, b, repeat=2)
print(list(prod))

from itertools import permutations

# Permutations of a list
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

# Permutations of length 2
perm = permutations(a, 2)
print(list(perm))

from itertools import combinations

# Combinations of a list of length 2
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))

from itertools import combinations_with_replacement

# Combinations with replacement
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

from itertools import accumulate

# Accumulate values in a list
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)  # Prints the original list
print(list(acc))  # Prints accumulated values

import operator

# Accumulate using multiplication
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)
print(list(acc))

# Accumulate using maximum function
a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(a)
print(list(acc))

from itertools import groupby

# Group elements based on a condition
def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

# Group using a lambda function
group_obj = groupby(a, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

# Grouping a list of dictionaries based on a key
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

from itertools import count, cycle, repeat

# Infinite counting
for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3]

# Cycling through a list repeatedly
for i in cycle(a):
    print(i)
    break

# Repeating a value
for i in repeat(2, 4):
    print(i)
