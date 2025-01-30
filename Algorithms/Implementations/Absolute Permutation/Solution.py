#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    # Check if a valid permutation is possible
    if (k == 0) or (k != 0 and n % (2 * k) == 0):
        orig = []
        
        # Create a list of numbers from 1 to n
        for i in range(1, n + 1):
            orig.append(i)
        
        # If k is not 0, perform the permutation by adding and subtracting k
        if k != 0:
            i = 0
            # Iterate through the list in blocks of 2 * k
            for j in range(n // (2 * k)):
                # Add k to the first k elements in the block
                for l in range(k):
                    orig[i] += k
                    i += 1
                # Subtract k from the next k elements in the block
                for l in range(k):
                    orig[i] -= k
                    i += 1
        return orig  # Return the permutation
    else:
        # If the condition isn't met, return [-1] indicating no valid permutation
        return [-1]
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    # Loop for each test case
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        # Write the result as a space-separated string
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()