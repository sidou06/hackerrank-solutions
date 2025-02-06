#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def maximizingXor(l, r):
    # Write your code here
    maxi = 0
    # Iterate over all pairs (i, j) where l <= i <= j <= r
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            # Compute XOR and update maximum if needed
            if i ^ j > maxi:
                maxi = i ^ j
    return maxi 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the lower bound l
    l = int(input().strip())

    # Read the upper bound r
    r = int(input().strip())

    # Compute the maximum XOR value
    result = maximizingXor(l, r)

    # Write the result to output
    fptr.write(str(result) + '\n')

    fptr.close()