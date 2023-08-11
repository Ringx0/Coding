# Using lambda function to add 10 to a number
add10 = lambda x: x + 10
print(add10(5))

# Defining a function that adds 20 to a number
def add10_func(x):
    return x + 10

# Assigning the function to a new name
add10_key = add10_func
print(add10_key(5))

# Using lambda function to multiply two numbers
mult = lambda x, y: x * y
print(mult(2, 7))

# List of 2D points
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

# Sorting the list of points lexicographically
points2D_sorted = sorted(points2D)
print(points2D)
print(points2D_sorted)

# Sorting the list of points by the second element of each tuple
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D)
print(points2D_sorted)

# Function to extract the second element of a tuple
def sort_by_y(x):
    return x[1]

# Sorting using the custom sort function
points2D_sorted = sorted(points2D, key=sort_by_y)
print(points2D)
print(points2D_sorted)

# Sorting by the sum of elements in each tuple
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D)
print(points2D_sorted)

# List of numbers
a = [1, 2, 3, 4, 5, 6]

# Using map with lambda to double each element
b = map(lambda x: x * 2, a)
print(list(b))

# Using list comprehension to double each element
c = [x * 2 for x in a]
print(c)

# Using filter with lambda to keep even numbers
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

# Using list comprehension to keep even numbers
c = [x for x in a if x % 2 == 0]
print(c)

# Using reduce to calculate the product of all elements
from functools import reduce
product_a = reduce(lambda x, y: x * y, a)
print(product_a)
