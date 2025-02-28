#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. LONG_INTEGER k
#  4. INTEGER m
#

def solve(a, b, k, m):
    # Perform the first loop to handle even values of k
    while k % 2 == 0:
        # Compute new values of a and b using modular arithmetic
        a, b = (a ** 2 - b ** 2) % m, (2 * a * b) % m  
        k //= 2  # Halve k

    # Initialize c and d with the current values of a and b
    c, d = a, b  
    k //= 2  # Further halve k

    # Process remaining values of k
    while k > 0:
        # Compute the new a and b values
        a, b = (a ** 2 - b ** 2) % m, (2 * a * b) % m  

        # If k is odd, update c and d using matrix-like transformations
        if k % 2 == 1:
            c, d = (a * c - b * d) % m, (b * c + a * d) % m  

        k //= 2  # Halve k again

    # Return the final computed values as a list
    return [c, d]  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    q = int(input().strip())

    for q_itr in range(q):
        # Read input values
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        k = int(first_multiple_input[2])
        m = int(first_multiple_input[3])

        # Compute the result
        result = solve(a, b, k, m)

        # Write the result to output
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()