#!/bin/python3

import math  # Importing math module for mathematical operations
import os  # Importing os module for file handling
import random  # Importing random module (not used in this code)
import re  # Importing re module for regular expressions (not used in this code)
import sys  # Importing sys module for system-specific parameters

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER p
#

def solve(n, p):
    # Convert the input string n to an integer
    n = int(n)
    s = n  # Store original value of n
    res = 1  # Initialize result variable
    
    # Compute the product of ((n % p) + 1) for decreasing values of n
    while n > 0:
        res *= ((n % p) + 1)  # Multiply by (remainder + 1)
        n //= p  # Reduce n by dividing it by p
    
    return s + 1 - res  # Compute final result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open file for writing output

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):  # Iterate over test cases
        first_multiple_input = input().rstrip().split()  # Read input values

        n = first_multiple_input[0]  # Extract string n
        p = int(first_multiple_input[1])  # Extract integer p

        result = solve(n, p)  # Compute result

        fptr.write(str(result) + '\n')  # Write result to file

    fptr.close()  # Close file