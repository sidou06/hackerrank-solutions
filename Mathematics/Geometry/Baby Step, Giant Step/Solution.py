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
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER d
#

def solve(a, b, d):
    # If the target distance is 0, no steps are needed
    if d == 0:
        return 0

    # If the target distance is divisible by step size b, take exact steps
    if d % b == 0:
        return d // b

    # If target equals a, then we only need one step of a
    if d == a:
        return 1

    # If target is smaller than b and not equal to a,
    # we need at least two steps to reach or overshoot it
    if d < b:
        return 2

    # Otherwise, take the maximum possible full b-steps and one extra to cover the rest
    return d // b + 1

if __name__ == '__main__':
    # Open the output file path
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of queries
    q = int(input().strip())

    for q_itr in range(q):
        # Read each query parameters a, b, and d
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        d = int(first_multiple_input[2])

        # Call the solve function for the current query
        result = solve(a, b, d)

        # Write result to output file
        fptr.write(str(result) + '\n')

    fptr.close()