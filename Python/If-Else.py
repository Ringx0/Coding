#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
# n % 2 = 0 used to determine if integer 'n' is even
if (n % 2) != 0:
    print("Weird")
else:
    if n >= 2 and n <= 5:
        print ("Not Weird")
    if n >= 6 and n <= 20:
        print ("Weird")
    if n > 20 and n <=100:
        print ("Not Weird")
