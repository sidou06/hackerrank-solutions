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
# The function accepts LONG_INTEGER n as parameter.
#

def solve(n):
    # Calculate d such that d * (d + 1) / 2 = n
    d = int(math.sqrt(2 * n))  # Estimate the value of d using square root

    # Check if the sum of first d natural numbers equals n
    if d * (d + 1) == 2 * n:
        return "Go On Bob " + str(d)  # Return success message with value of d
    return "Better Luck Next Time"  # Return failure message if not a perfect match

if __name__ == '__main__':
    # Open output file as defined in environment
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())  # Read input number for this test case

        result = solve(n)  # Get result by calling solve()

        fptr.write(result + '\n')  # Write result to output file

    fptr.close()