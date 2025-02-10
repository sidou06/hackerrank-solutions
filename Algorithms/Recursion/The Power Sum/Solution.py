#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N, start=1):
    # Initialize count of valid combinations
    count = 0
    
    # Debug print statement (likely used for testing)
    print(X, N, start)

    # If the smallest power is greater than X, no valid combinations exist
    if pow(start, N) > X:
        return count

    # Check if X itself is a perfect power of N
    if pow(int(pow(X, 1/N)), N) == X or pow(int(pow(X, 1/N)) + 1, N) == X:
        print("here")  # Debug print
        count += 1

    # Iterate over potential bases to check valid power sums
    while pow(start, N) < X:
        start += 1
        count += powerSum(X - pow(start - 1, N), N, start)

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values
    X = int(input().strip())
    N = int(input().strip())

    # Compute the result
    result = powerSum(X, N)

    # Write output result to file
    fptr.write(str(result) + '\n')
    fptr.close()