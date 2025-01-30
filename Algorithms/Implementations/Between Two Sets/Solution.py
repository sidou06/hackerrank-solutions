#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Sort the arrays a and b
    a.sort()
    b.sort()
    
    # Find the maximum value that can be a multiple of the last element in a
    x = b[0] // a[-1]
    cpt = 0
    i = 1
    
    # Loop to find possible values of x that satisfy the conditions
    while i <= x:
        boo = True
        w = i * a[-1]
        
        # Check if w is a multiple of all elements in array a
        j = 0
        while j < len(a) and boo:
            if w % a[j] != 0:
                boo = False
            j += 1
        
        # Check if w is a divisor of all elements in array b
        k = 0
        while k < len(b) and boo:
            if b[k] % w != 0:
                boo = False
            k += 1
        
        # If w satisfies both conditions, increment the counter
        if boo:
            cpt += 1
        
        i += 1
    
    return cpt
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values for array sizes
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    # Read input arrays
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    # Call the function to get the total count
    total = getTotalX(arr, brr)

    # Write the result to the output file
    fptr.write(str(total) + '\n')

    fptr.close()