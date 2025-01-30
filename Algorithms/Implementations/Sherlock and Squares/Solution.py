#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Calculate the square root of a and b
    r1 = math.sqrt(a)
    r2 = math.sqrt(b)
    
    # If the square root of a is an integer, count it as a perfect square
    if r1.is_integer():
        return int(r2 - r1 + 1)
    else:
        # Count the number of perfect squares between a and b (inclusive)
        return int(r2) - int(r1)

if __name__ == '__main__':
    # Open the output file
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    q = int(input().strip())

    for q_itr in range(q):
        # Read the values of a and b
        first_multiple_input = input().rstrip().split()
        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])

        # Call the squares function
        result = squares(a, b)

        # Write the result to the output file
        fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()