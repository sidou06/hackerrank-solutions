#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Flip all the bits by subtracting n from the maximum 32-bit unsigned integer value (2^32 - 1)
    return 2 ** 32 - 1 - n 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())  # Read number of test cases

    for q_itr in range(q):
        n = int(input().strip())  # Read input value

        result = flippingBits(n)  # Compute the result

        fptr.write(str(result) + '\n')  # Write result to output

    fptr.close()