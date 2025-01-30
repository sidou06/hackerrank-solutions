#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Initialize an empty list to store the results.
    res = []
    
    # Iterate through the range of numbers from 1 to n (inclusive).
    for i in range(len(p)):
        # Find the position of the element in p that gives the desired equation result
        # p.index(i + 1) finds the index of the element i + 1 in the array p.
        # Adding 1 to the result because positions in the array are 1-based.
        res.append(p.index((p.index(i + 1)) + 1) + 1)
    
    # Return the list of results
    return res

if __name__ == '__main__':
    # Open the output file to write the result.
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values.
    n = int(input().strip())  # Length of the array
    p = list(map(int, input().rstrip().split()))  # The permutation array

    # Call the permutationEquation function and get the result.
    result = permutationEquation(p)

    # Write the result to the output file.
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    # Close the output file after writing the results.
    fptr.close()