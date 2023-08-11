from collections import Counter

# Create a string 'a' with some characters
a = "aaaaabbbbccc"

# Create a Counter object to count occurrences of each character in 'a'
my_counter = Counter(a)

# Print the Counter object
print(my_counter)

# Print the items (key-value pairs) in the Counter
print(my_counter.items())

# Print the keys in the Counter
print(my_counter.keys())

# Print the values in the Counter
print(my_counter.values())

# Print the most common element (character) in the Counter
print(my_counter.most_common(1))

# Print the two most common elements in the Counter
print(my_counter.most_common(2))

# Print the most common element and its count using indexing
print(my_counter.most_common(1)[0])

# Print the most common element (character) using indexing
print(my_counter.most_common(1)[0][0])

# Get an iterator for the elements in the Counter
print(my_counter.elements())

# Convert the elements iterator to a list
print(list(my_counter.elements()))

from collections import namedtuple

# Create a named tuple 'Point' with fields 'x' and 'y'
Point = namedtuple('Point', 'x,y')

# Create an instance of the Point named tuple
pt = Point(1, -4)

# Print the Point named tuple
print(pt)

# Access the 'x' and 'y' fields of the named tuple
print(pt.x, pt.y)

from collections import OrderedDict

# Create an ordered dictionary
ordered_dict = OrderedDict()

# Add key-value pairs to the ordered dictionary
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

# Print the ordered dictionary
print(ordered_dict)

# Create a regular dictionary (unordered)
ordered_dict = {}

# Add key-value pairs to the regular dictionary
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

# Print the regular dictionary
print(ordered_dict)

from collections import defaultdict

# Create a defaultdict with default value type 'int'
d = defaultdict(int)

# Add key-value pairs to the defaultdict
d['a'] = 1
d['b'] = 2

# Print the defaultdict
print(d)

# Access values using keys even if the key is not present
print(d['a'])
print(d['b'])
print(d['c'])  # Default value (0) is returned for missing key

# Create a defaultdict with default value type 'list'
d = defaultdict(list)
d['a'] = 1
d['b'] = 2

# Print the defaultdict
print(d)

# Access values using keys even if the key is not present
print(d['a'])
print(d['b'])
print(d['c'])  # Default value (empty list) is returned for missing key

from collections import deque

# Create a deque (double-ended queue)
d = deque()

# Append elements to the right end of the deque
d.append(1)
d.append(2)
print(d)

# Append an element to the left end of the deque
d.appendleft(3)
print(d)

# Remove and return an element from the right end of the deque
d.pop()
print(d)

# Remove and return an element from the left end of the deque
d.popleft()
print(d)

# Clear all elements from the deque
d.clear()
print(d)

# Append elements to the right end of the deque
d.append(7)
d.extend([4, 5, 6])
print(d)

# Extend the deque by appending elements to the left end
d.extendleft([5, 6])
print(d)

# Rotate the deque to the right by one step
d.rotate(1)
print(d)

# Rotate the deque to the left by two steps
d.rotate(-2)
print(d)
