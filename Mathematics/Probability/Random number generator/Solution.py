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
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#

def solve(a, b, c):
    # Write your code here

    # Find the smaller and larger of a and b
    x = min(a, b)
    y = max(a, b) 
    
    # Case 1: if c is smaller than x
    if c < x:
        n = c * c  # numerator
        d = 2 * x * y  # denominator
    
    # Case 2: if c is between x and y
    elif c < y:
        n = 2 * c - x  # numerator
        d = 2 * y  # denominator
    
    # Case 3: if c is between y and x + y
    elif c < x + y:
        n = 2 * x * y - (x + y - c) ** 2  # numerator
        d = 2 * x * y  # denominator
    
    # Case 4: if c is greater than or equal to x + y
    else:
        n = 1  # numerator
        d = 1  # denominator
    
    # Reduce the fraction by their greatest common divisor
    g = math.gcd(n, d) 
    n //= g 
    d //= g 
    
    # Return the fraction as a string
    return (str(n) + "/" + str(d)) 

if __name__ == '__main__':
    # Open output file for writing
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    n = int(input().strip())

    # Process each test case
    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        c = int(first_multiple_input[2])

        result = solve(a, b, c)

        # Write the result to the output file
        fptr.write(result + '\n')

    # Close the output file
    fptr.close()