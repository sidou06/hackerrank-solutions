#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameWithCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n (number of rows)
#  2. INTEGER m (number of columns)
#

def gameWithCells(n, m):
    # Calculate the minimum number of supply drops needed
    # Each drop covers a 2x2 region, so we divide the grid into 2x2 blocks
    return ((n+1) // 2) * ((m+1) // 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values for grid dimensions
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    # Compute the result using the function
    result = gameWithCells(n, m)

    # Write the result to output
    fptr.write(str(result) + '\n')

    fptr.close()