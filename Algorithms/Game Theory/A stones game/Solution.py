#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'half' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

from math import frexp

def half(n):
    # Check if n is odd
    if n&1: 
        return 1
    # Perform bitwise operations to calculate the result
    x = 1^int(frexp(n)[1])
    y = 1 << int(frexp(x)[1] - 1)
    # Return the calculated value based on the condition
    return 1 << y - 2 if (x ^ y) + 1 == y else (1 << y - 1) - (1 << (x ^ y)) + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of test cases
    t = int(input().strip())

    # Iterate through the test cases
    for t_itr in range(t):
        # Read the input integer n
        n = int(input().strip())

        # Get the result of the half function
        result = half(n)

        # Write the result to the output file
        fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()