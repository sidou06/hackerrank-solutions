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
#  1. INTEGER x1
#  2. INTEGER y1
#  3. INTEGER x2
#  4. INTEGER y2
#

def solve(x1, y1, x2, y2):
    # Calculate the differences in x and y coordinates
    y = y2 - y1
    x = x2 - x1 

    # If the two points are the same, return 0 (no points in between)
    if x == 0 and y == 0:
        return 0 

    # If the points are on the same vertical line, return the number of points between them
    if x == 0:
        return (abs(y) - 1)

    # If the points are on the same horizontal line, return the number of points between them
    if y == 0:
        return (abs(x) - 1)

    # Compute the greatest common divisor (gcd) of x and y
    g = math.gcd(x, y)

    # Reduce x by the gcd factor
    d = x // g 
    x //= d

    # Return the number of integer points between the two given points
    return x - 1 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        # Read the input values
        first_multiple_input = input().rstrip().split()

        x1 = int(first_multiple_input[0])
        y1 = int(first_multiple_input[1])
        x2 = int(first_multiple_input[2])
        y2 = int(first_multiple_input[3])

        # Compute and write the result
        result = solve(x1, y1, x2, y2)
        fptr.write(str(result) + '\n')

    fptr.close()