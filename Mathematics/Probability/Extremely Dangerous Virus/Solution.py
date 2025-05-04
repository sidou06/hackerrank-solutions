#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. LONG_INTEGER t
#

# Define modulo constant
m = 10 ** 9 + 7 

def solve(a, b, t):
    # Compute the average of a and b
    # Raise the result to the power of t modulo m
    return pow((a + b) // 2, t, m)

if __name__ == '__main__':
    # Open the output file using the path from environment variable
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values for a, b, and t
    first_multiple_input = input().rstrip().split()

    a = int(first_multiple_input[0])
    b = int(first_multiple_input[1])
    t = int(first_multiple_input[2])

    # Call the solve function
    result = solve(a, b, t)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()