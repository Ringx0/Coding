# Create a tuple containing three elements and print it.
mytuple = ("Max", 28, "Boston")
print(mytuple)

# Create a tuple using tuple packing and print it.
mytuple = "Max", 28, "Boston"
print(mytuple)

# Create a variable mytuple with a single value "Max".
# Note that this does not create a tuple because a comma is missing.
mytuple = ("Max")
# Print the type of mytuple, which will be <class 'str'> due to missing comma.
print(type(mytuple))

# Create a tuple with a single element "Max" and print its type.
mytuple = ("Max",)
# Print the type of mytuple, which will be <class 'tuple'>.
print(type(mytuple))

# Create a tuple using the tuple constructor and print it.
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

# Access and print individual items in the tuple.
item = mytuple[0]  # Access the first item "Max".
print(item)
item = mytuple[1]  # Access the second item 28.
print(item)
item = mytuple[-1]  # Access the last item "Boston".
print(item)

# Try to modify an item in the tuple (this will result in an error).
# Tuples are immutable, so individual elements cannot be changed.
# This line will raise a TypeError.
# mytuple[0] = "Tim"

# Loop through the tuple and print each item.
for i in mytuple:
    print(i)

# Check if "Max" is in the tuple and print the result.
if "Max" in mytuple:
    print("yes")
else:
    print("no")

# Get the length of the tuple and print it.
print(len(mytuple))

# Count occurrences of 'p' in the tuple and print the result.
print(mytuple.count('p'))

# Get the index of the first occurrence of 'p' and print the result.
print(mytuple.index('p'))

# Convert the tuple to a list and print it.
my_list = list(mytuple)
print(my_list)

# Convert the list back to a tuple and print it.
my_tuple2 = tuple(my_list)
print(my_tuple2)

# Create a tuple of integers and slice it, then print the slices.
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]  # Slice from index 2 to 4 (inclusive).
print(b)
b = a[::2]  # Slice with step 2.
print(b)
b = a[::-1]  # Reverse the tuple.
print(b)

# Create a tuple using tuple packing.
my_tuple = "Max", 28, "Boston"

# Unpack the tuple into separate variables and print them.
name, age, city = my_tuple
print(name)
print(age)
print(city)

# Unpack a tuple with extended unpacking and print the values.
my_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple
print(i1)
print(i3)
print(i2)

# Import the sys module to get memory size information.
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)

# Print the memory size of the list and tuple.
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# Import the timeit module to measure execution time.
import timeit

# Print the time taken to create a list and tuple.
print(timeit.timeit(stmt="[0, 1, 2, 3,  4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3,  4, 5)", number=1000000))
