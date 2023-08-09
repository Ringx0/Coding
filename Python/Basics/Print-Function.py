n = int(input())  # Read the integer 'n' from the user input and convert it to an integer.

# Generate a list of integers from 1 to 'n' using a loop and convert each number to a string.
numbers = [str(i) for i in range(1, n + 1)]

# Concatenate the numbers in the list without spaces, converting the list to a single string.
output = ''.join(numbers)

# Print the final concatenated string.
print(output)
