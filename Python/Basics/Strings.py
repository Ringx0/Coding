# Creating a string and printing it
my_string = "Hello World"
print(my_string)

# Creating a string with a single quote and escaping it with a backslash
my_string = 'I\'m a programmer'
print(my_string)

# Creating a multi-line string using triple quotes
my_string = """Hello
World"""
print(my_string)

# Creating a multi-line string using a backslash for line continuation
my_string = """Hello \
World"""
print(my_string)

# Accessing characters in a string
my_string = "Hello World"
char = my_string[0]  # Accessing the first character ('H')
print(char)

char = my_string[-1]  # Accessing the last character ('d')
print(char)

# Slicing a substring from the string
substring = my_string[1:5]
print(substring)

# Reversing the string using slicing
substring = my_string[::-1]
print(substring)

# Combining strings using concatenation
greeting = "Hello"
name = "Pawel"
sentence = greeting + " " + name
print(sentence)

# Iterating through the characters of a string
for i in greeting:
    print(i)

# Checking if a character is present in the string
if 'e' in greeting:
    print("yes")
else:
    print("no")

# Stripping whitespace characters from the string
my_string = '    Hello World    '
print(my_string)
my_string = my_string.strip()
print(my_string)

# Converting the string to uppercase and lowercase
print(my_string.upper())
print(my_string.lower())

# Checking if the string starts with 'H' and ends with 'd'
print(my_string.startswith('H'))
print(my_string.endswith('d'))

# Finding the index of the first occurrence of 'o'
print(my_string.find('o'))

# Counting occurrences of 'l' in the string
print(my_string.count('l'))

# Replacing 'World' with 'Universe' in the string
print(my_string.replace('World', 'Universe'))

# Splitting a string into a list of words
my_string = 'how are you doing'
my_list = my_string.split()
print(my_list)

# Splitting a string using a custom delimiter (comma)
my_string = 'how,are,you,doing'
my_list = my_string.split(",")
print(my_list)

# Joining the list elements with a space delimiter to create a new string
new_string = ' '.join(my_list)
print(new_string)

# Creating a list with repeated elements and printing it
my_list = ['a'] * 6
print(my_list)

# Concatenating list elements using string concatenation (bad approach)
from timeit import default_timer as timer

start = timer()
my_string = ''  # Initialize an empty string
for i in my_list:
    my_string += i  # Inefficient string concatenation
print(my_string)
stop = timer()
print(stop - start)

# Concatenating list elements using the join method (better approach)
start = timer()
my_string = ''.join(my_list)  # Joining elements using an efficient method
print(my_string)
stop = timer()
print(stop - start)

# Using string formatting to insert a variable value
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

# Using string formatting with an integer variable
var = 3
my_string = "the variable is %d" % var
print(my_string)

# Using string formatting with a floating-point variable
var = 3.1415
my_string = "the variable is %.2f" % var
print(my_string)

# Using string formatting with curly braces to insert a variable
my_string = "the variable is {}".format(var)
print(my_string)

# Using string formatting with specified precision and multiple variables
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var, var2)
print(my_string)

# Using f-strings (formatted string literals) to insert variables directly
my_string = f"the variable is {var * 2} and {var2}"
print(my_string)
