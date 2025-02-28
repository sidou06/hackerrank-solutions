#!/bin/python3

import os
import sys

#
# Complete the 'strangeGrid' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER r
#  2. INTEGER c
#

def strangeGrid(r, c):
    return (10 * ((r - 1) // 2)) + (1 * (r % 2 == 0)) + (2 * (c - 1))  # Compute and return the grid value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])  # Read row number
    c = int(first_multiple_input[1])  # Read column number

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')  # Write the result to output

    fptr.close()