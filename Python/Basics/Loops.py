if __name__ == '__main__':
    n = int(input())  # Read the integer 'n' from the user input and convert it to an integer.

# Check if 'n' is within the range [1, 20]
if 1 <= n <= 20:
    # If 'n' is within the range, perform a loop from 0 to 'n-1'
    for n in range(n):
        print(n*n)  # Print the square of 'n' (the loop variable)
        n -= 1  # Decrease the value of 'n' by 1 in each iteration of the loop
