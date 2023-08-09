# Creating a set with elements 1, 2, and 3
myset = {1, 2, 3}
print(myset)

# Creating a set with elements 1, 2, 3 (duplicate elements are automatically removed)
myset = {1, 2, 3, 1, 2}
print(myset)

# Creating a set from a list with elements 1, 2, and 3
myset = set([1, 2, 3])
print(myset)

# Creating a set from the characters of the string "Hello"
myset = set("Hello")
print(myset)

# Creating an empty dictionary (not a set). Note: This line creates an empty dictionary, not an empty set.
myset = {}
print(type(myset))

# Creating an empty set and adding elements 1, 2, and 3
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

# Removing element 3 from the set
myset.remove(3)
print(myset)

# Discarding element 3 from the set (no error if not found)
myset.discard(3)
print(myset)

# Clearing all elements from the set
myset.clear()
print(myset)

# Creating a set with elements 1, 2, and 3
myset = {1, 2, 3}
# Removing and returning an arbitrary element from the set
print(myset.pop())
print(myset)

# Iterating through the set and printing each element
for i in myset:
    print(i)

# Checking if the value 2 is present in the set
if 2 in myset:
    print("yes")

# Creating sets for odd numbers, even numbers, and prime numbers
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# Union of odd and even sets
u = odds.union(evens)
print(u)

# Intersection of odd and even sets
i = odds.intersection(evens)
print(i)

# Intersection of odd and prime sets
i = odds.intersection(primes)
print(i)

# Intersection of even and prime sets
i = evens.intersection(primes)
print(i)

# Creating two sets, setA and setB
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# Finding the difference between setA and setB
diff = setA.difference(setB)
print(diff)

# Finding the difference between setB and setA
diff = setB.difference(setA)
print(diff)

# Finding the symmetric difference between setA and setB
diff = setB.symmetric_difference(setA)
print(diff)

# Updating setA by adding elements from setB
setA.update(setB)
print(setA)

# Updating setA to contain only elements present in both setA and setB
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.intersection_update(setB)
print(setA)

# Updating setA to remove elements present in setB
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.difference_update(setB)
print(setA)

# Updating setA to contain the symmetric difference of setA and setB
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.symmetric_difference_update(setB)
print(setA)

# Creating sets setA, setB, and setC, and checking subset, superset, and disjoint relationships
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}

print(setA.issubset(setB))
print(setB.issubset(setA))

print(setA.issuperset(setB))
print(setB.issuperset(setA))

print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))

# Assigning setB to reference the same set as setA
setB = setA
print(setB)

# Adding an element to setB affects setA as well
setB.add(7)
print(setA)
print(setB)

# Creating sets setA and setB, and copying setA to setB
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}

# Copying setA to setB (both sets reference the same values)
setB = setA.copy()
# Alternatively, you can create a new set containing the same values as setA
setB = set(setA)

# Adding an element to setB does not affect setA
setB.add(7)
print(setA)
print(setB)

# Creating a frozenset (an immutable version of a set)
a = frozenset([1, 2, 3, 4])
print(a)

# Performing a union between a frozenset and a regular set
u = a.union(setA)
print(u)
