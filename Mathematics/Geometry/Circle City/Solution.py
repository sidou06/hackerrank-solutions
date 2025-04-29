#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER k
#

def solve(d, k):
    # Calculate the radius from the given squared distance
    r = math.sqrt(d) 

    # Initialize result counter
    res = 0

    # Set a limit for iteration to avoid redundant checks (based on symmetry)
    lim = int(math.sqrt(d // 2))

    # Iterate over all possible 'a' values from 0 to lim
    for a in range(0, lim + 1):
        # Compute b² = d - a²
        b2 = d - a ** 2
        b = math.sqrt(b2) 

        # If b is a perfect square, then (a, b) is a valid integer pair on the circle
        if int(b) == b:
            res += 4  # Count (±a, ±b)

            # If a ≠ b and a ≠ 0, we can add (±b, ±a) as well (ensuring no duplicates)
            if a != b and a != 0:
                res += 4

    # If fewer points than required, return "impossible"
    if k < res:
        return "impossible"

    # Otherwise, it's "possible"
    return "possible"

# Entry point of the program
if __name__ == '__main__':
    # Open output file to write results
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of test cases
    t = int(input().strip())

    # Process each test case
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])  # Distance squared
        k = int(first_multiple_input[1])  # Required number of lattice points

        result = solve(d, k)

        # Write result to output
        fptr.write(result + '\n')

    # Close output file
    fptr.close()