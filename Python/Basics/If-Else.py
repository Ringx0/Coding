import math
import os
import random
import re
import sys

n = int(input().strip())  # Read the input integer and store it in the variable 'n'

# Check if the integer 'n' is odd (not divisible by 2)
if (n % 2) != 0:
    print("Weird")  # If 'n' is odd, print "Weird"
else:
    # If 'n' is even (divisible by 2), check various ranges for the value of 'n'
    if n >= 2 and n <= 5:
        print("Not Weird")  # If 'n' is even and within the range [2, 5], print "Not Weird"
    if n >= 6 and n <= 20:
        print("Weird")  # If 'n' is even and within the range [6, 20], print "Weird"
    if n > 20 and n <= 100:
        print("Not Weird")  # If 'n' is even and within the range (20, 100], print "Not Weird"
