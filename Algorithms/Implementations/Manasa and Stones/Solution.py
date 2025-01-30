#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
    # Calculate the absolute difference between a and b
    diff = abs(a - b)
    
    # Initialize pr as the product of the smaller value of a or b and (n - 1)
    pr = min(a, b) * (n - 1)
    
    # Create a result list with the initial value pr
    res = [pr]
    
    # Generate the rest of the possible values by iterating from 1 to n-1
    for j in range(1, n):
        res.append(pr + j * diff)  # Add the next possible value to the result list
    
    # Remove duplicates from the result list by converting it to a set, then back to a list
    res = list(set(res))
    
    # Sort the list in ascending order
    res.sort()
    
    # Return the sorted list of results
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    T = int(input().strip())

    # Loop over each test case
    for T_itr in range(T):
        # Read the values for n, a, and b for the current test case
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())

        # Call the stones function to calculate the result
        result = stones(n, a, b)

        # Write the result to the output file, joined by spaces
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()