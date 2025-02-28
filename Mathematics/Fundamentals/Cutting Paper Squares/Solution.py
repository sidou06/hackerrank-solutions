#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def solve(n, m):
    # Determine the larger and smaller values between n and m
    big = max(n, m)
    small = min(n, m)
    
    # Compute the minimum number of cuts needed
    return (big * small - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values for n and m
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    # Compute and write the result
    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()