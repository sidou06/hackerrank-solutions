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
# The function accepts INTEGER_ARRAY a as parameter.
#

def solve(a):
    # Initialize flag to track if an odd number is found
    odd = False 
    
    # Define modulo value to prevent overflow
    mod = 10 ** 9 + 7  
    
    # Initialize result variable
    res = 1  
    
    # Iterate through the array
    for i in range(len(a)):
        res *= 2  # Multiply result by 2 for each element
        
        # If an odd number is found and no previous odd was found
        if a[i] % 2 == 1 and not odd:
            odd = True  # Mark that an odd number has been found
            res //= 2  # Divide result by 2 once
        
        res %= mod  # Apply modulo operation to keep result within limits
    
    res -= 1  # Subtract 1 from the final result
    return res  # Return the computed value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file

    a_count = int(input().strip())  # Read number of elements

    a = list(map(int, input().rstrip().split()))  # Read the array

    result = solve(a)  # Call the function and get result

    fptr.write(str(result) + '\n')  # Write result to output file

    fptr.close()  # Close the file