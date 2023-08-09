# Create a list of strings and print it.
mylist = ["banana", "apple", "cherry"]
print(mylist)

# Create a list with mixed data types and print it.
mylist2 = [5, True, "apple", "apple"]
print(mylist2)

# Access the last item in mylist and print it.
item = mylist[-1]
print(item)

# Print each item in mylist using a loop.
for i in mylist:
    print(i)

# Check if "banana" is in mylist and print the result.
if "banana" in mylist:
    print("yes")
else:
    print("no")

# Print the length of mylist.
print(len(mylist))

# Append "lemon" to mylist and print the updated list.
mylist.append("lemon")
print(mylist)

# Insert "orange" at index 1 in mylist and print the updated list.
mylist.insert(1, "orange")
print(mylist)

# Remove and print the last item from mylist.
item = mylist.pop()
print(item)
print(mylist)

# Remove "cherry" from mylist and print the updated list.
mylist.remove("cherry")
print(mylist)

# Clear mylist and print the empty list.
mylist.clear()
print(mylist)

# Create a new mylist and reverse it, then print it.
mylist = ["banana", "apple", "cherry"]
mylist.reverse()
print(mylist)

# Create a list of integers, print it, and sort it.
mylist = [1, 2, 6, -1, -5, 10, 9]
print(mylist)
sorted_list = sorted(mylist)
print(sorted_list)
mylist.sort()
print(mylist)

# Create a list of zeros and print it.
mylist2 = [0] * 5
print(mylist2)

# Create a list and print it.
mylist3 = [1, 2, 3, 4, 5]
print(mylist3)

# Concatenate mylist2 and mylist3 and print the result.
new_list = mylist2 + mylist3
print(new_list)

# Create a list of integers and slice it, then print each slice.
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[:5]
print(a)
a = mylist[1:]
print(a)
a = mylist[0:9]
print(a)
a = mylist[::-1]
print(a)
a = mylist[::2]
print(a)

# Demonstrate various methods of copying a list and modifying the copies.
list_org = ["banana", "cherry", "apple"]

# Both list_cpy and list_org refer to the same list in memory.
list_cpy = list_org
list_cpy.append("lemon")
print(list_cpy)
print(list_org)

# Create copies of the list using different methods.
list_cpy2 = list_org.copy()
list_cpy2 = list(list_org)
list_cpy2 = list_org[:]

# Modify the copy and show that the original list remains unchanged.
list_cpy2.append("mango")
print(list_cpy2)
print(list_org)

# Create a list of integers and square each element to create a new list.
mylist = [1, 2, 3, 4, 5, 6]
b = [i * i for i in mylist]

# Print the original list and the squared list.
print(mylist)
print(b)
