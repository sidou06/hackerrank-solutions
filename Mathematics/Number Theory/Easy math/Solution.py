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
# The function accepts INTEGER x as parameter.
#

def solve(x):
    # Function to compute the smallest integer satisfying given conditions
    twos = 0  # Count of factor 2 in x
    fives = 0  # Count of factor 5 in x
    
    # Count the number of times x is divisible by 2
    while x % 2 == 0:
        twos += 1 
        x //= 2 
    
    # Count the number of times x is divisible by 5
    while x % 5 == 0:
        fives += 1
        x //= 5 
    
    # Compute b, which adjusts for trailing zeros
    b = max(twos - 2, fives) 
    a = 1  # Counter for finding the smallest number that meets the conditions
    big = 1  # Initial value of the number formed by repeating ones
    
    # Find the smallest multiple of x formed by repeating ones
    while big % x != 0:
        big = (big * 10 + 1) % x  # Generate next number in the sequence
        a += 1  # Increment count
    
    return 2 * a + b  # Compute the final result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open file for writing output

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):  # Iterate through test cases
        x = int(input().strip())  # Read input integer
        result = solve(x)  # Compute result
        print(result)  # Print result to console
        fptr.write(str(result) + '\n')  # Write result to file

    fptr.close()  # Close file