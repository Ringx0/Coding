# Create a dictionary with key-value pairs and print it.
mydict = {"name": "Pawel", "age": 26, "city": "Galway"}
print(mydict)

# Create a dictionary using dict constructor and print it.
mydict2 = dict(name="Mary", age=27, city="Dublin")
print(mydict2)

# Access and print values using keys from the dictionary.
value = mydict["name"]
print(value)
value = mydict["age"]
print(value)

# Add a new key-value pair to the dictionary and print it.
mydict["email"] = "pawel@gmail.com"
print(mydict)

# Modify an existing key's value and print the updated dictionary.
mydict["email"] = "pawel25@gmail.com"
print(mydict)

# Delete a key-value pair from the dictionary and print it.
del mydict["name"]
print(mydict)

# Remove a key-value pair using the pop method and print the dictionary.
mydict.pop("age")
print(mydict)

# Remove and print an arbitrary key-value pair using popitem.
mydict.popitem()
print(mydict)

# Check if a key exists in the dictionary and print its value.
mydict = {"name": "Pawel", "age": 26, "city": "Galway"}
if "name" in mydict:
    print(mydict["name"])

# Try to access a nonexistent key, print an error message in exception.
try:
    print(mydict["name"])
except:
    print("Error")

# Loop through the dictionary keys and print each key.
for key in mydict:
    print(key)

# Loop through the dictionary keys using the keys() method and print them.
for key in mydict.keys():
    print(key)

# Loop through the dictionary values and print each value.
for value in mydict.values():
    print(value)

# Loop through the dictionary items and print key-value pairs.
for key, value in mydict.items():
    print(key, value)

# Create a copy of the dictionary that points to the same memory location.
mydict_cpy = mydict

# Modify the copied dictionary and observe the change in the original.
mydict_cpy["email"] = "pawel@gmail.com"
print(mydict_cpy)
print(mydict)

# Create a shallow copy of the dictionary using the copy() method.
mydict = {"name": "Pawel", "age": 26, "city": "Galway"}
mydict_cpy = mydict.copy()

# Modify the copied dictionary and observe that the original remains unchanged.
mydict_cpy["email"] = "pawel@gmail.com"
print(mydict_cpy)
print(mydict)

# Merge dictionaries using the update() method and print the result.
my_dict = {"name": "Pawel", "age": 26, "email": "pawel@gmail.com"}
my_dict_2 = dict(name="Mary", age=27, city="Dublin")
my_dict.update(my_dict_2)
print(my_dict)

# Create a dictionary with numeric keys and print it.
my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

# Access and print values using numeric keys.
value = my_dict[3]
print(value)

# Create a tuple and use it as a key in the dictionary.
mytuple = (8, 7)
mydict = {mytuple: 15}
print(mydict)
