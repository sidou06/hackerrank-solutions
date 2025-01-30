#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Initialize a counter for the number of ways to split the segment
    nb = 0
    
    # Loop through all possible starting points of the segment
    for k in range(len(s) - m + 1):
        # Calculate the sum of the current segment of length m
        suu = sum(s[k:k+m])
        
        # If the sum matches d, increment the counter
        if suu == d:
            nb += 1
    
    return nb

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of elements in the array
    n = int(input().strip())

    # Read the array s
    s = list(map(int, input().rstrip().split()))

    # Read d and m
    first_multiple_input = input().rstrip().split()
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    # Get the result from the function
    result = birthday(s, d, m)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    fptr.close()