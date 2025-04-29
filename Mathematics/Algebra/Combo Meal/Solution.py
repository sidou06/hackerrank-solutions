#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'profit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts the following parameters:
#  1. INTEGER b - base value (possibly fixed income or investment)
#  2. INTEGER s - sales or revenue
#  3. INTEGER c - cost or expense
#

def profit(b, s, c):
    # Return the fixed profit calculated as base + sales - cost
    return b + s - c

if __name__ == '__main__':
    # Open the output file defined in the environment variable
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        # Read input values for b, s, c
        first_multiple_input = input().rstrip().split()
        b = int(first_multiple_input[0])  # Base value
        s = int(first_multiple_input[1])  # Sales value
        c = int(first_multiple_input[2])  # Cost value

        # Calculate profit
        result = profit(b, s, c)

        # Write result to output file
        fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()