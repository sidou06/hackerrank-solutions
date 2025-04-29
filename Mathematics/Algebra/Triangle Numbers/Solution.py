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
# The function accepts INTEGER n as parameter.
#

def solve(n):
    # If n is odd, return 2
    if n % 2 == 1:
        return 2

    # If n is even, and half of n is odd, return 4
    if (n // 2) % 2 == 1:
        return 4 

    # Otherwise, return 3
    return 3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file for writing

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        n = int(input().strip())  # Read input integer n

        result = solve(n)  # Get result from solve function

        fptr.write(str(result) + '\n')  # Write result to output file

    fptr.close()  # Close output file