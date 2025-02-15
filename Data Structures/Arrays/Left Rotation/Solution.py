#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Ensure d is within the array length
    d %= len(arr)  
    # Split the array into two parts: first d elements and the rest
    p1 = arr[:d]  
    p2 = arr[d:]  
    # Concatenate the two parts in reversed order
    return p2 + p1  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])  # Number of elements in array
    d = int(first_multiple_input[1])  # Number of rotations

    arr = list(map(int, input().rstrip().split()))  # Read the array

    # Compute the rotated array
    result = rotateLeft(d, arr)

    # Write the output to the file
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()