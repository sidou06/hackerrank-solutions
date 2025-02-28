#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. LONG_INTEGER a
#  2. LONG_INTEGER b
#  3. LONG_INTEGER x
#  4. LONG_INTEGER y
#

def solve(a, b, x, y):
    # Check if the greatest common divisor (GCD) of (a, b) is equal to the GCD of (x, y)
    if math.gcd(a, b) == math.gcd(x, y):
        return "YES"  # If they have the same GCD, return "YES"
    else:
        return "NO"   # Otherwise, return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        # Read input values
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])  # First integer
        b = int(first_multiple_input[1])  # Second integer
        x = int(first_multiple_input[2])  # Third integer
        y = int(first_multiple_input[3])  # Fourth integer

        # Get the result from the solve function
        result = solve(a, b, x, y)

        # Write the result to the output file
        fptr.write(result + '\n')

    fptr.close()