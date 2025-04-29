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
#  1. INTEGER d
#  2. INTEGER p
#

def solve(d, p):
    # Case 1: If d is negative, no valid solution exists
    if d < 0:
        return 0
    
    # Case 2: If d is zero
    elif d == 0:
        if p < 0:
            return 0  # No solution if product is negative
        elif p == 0:
            return 1  # Only one solution: both numbers are 0
        else:
            r = math.sqrt(p)
            if (int(r)) ** 2 == p:
                return 2  # Two solutions: (r, -r)
            else:
                return 0  # Not a perfect square, no solution
    
    # Case 3: If d is positive
    else:
        delta = d ** 2 + 4 * p  # Discriminant for solving x^2 + dx + p = 0
        if delta < 0:
            return 0  # No real solutions
        elif delta == 0:
            if d % 2 == 0:
                return 2  # One repeated solution (counted as 2)
            else:
                return 0  # Not even, root not integer
        else:
            r = math.sqrt(delta)
            if (int(r)) ** 2 != delta:
                return 0  # Not a perfect square, roots not rational
            else:
                cpt = 0
                x1 = 0 - d - r  # One root numerator
                x2 = r - d      # Another root numerator
                if x1 % 2 == 0:
                    cpt += 2  # Count both (x1, x2) and (x2, x1)
                if x2 % 2 == 0:
                    cpt += 2
                return cpt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file

    t = int(input().strip())  # Number of test cases

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])  # Read d
        p = int(first_multiple_input[1])  # Read p

        result = solve(d, p)

        fptr.write(str(result) + '\n')  # Write result

    fptr.close()  # Close output file