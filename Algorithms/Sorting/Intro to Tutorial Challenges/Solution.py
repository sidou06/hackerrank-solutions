#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'introTutorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER V
#  2. INTEGER_ARRAY arr
#

def introTutorial(V, arr):
    # Find the index of V in the array
    i = 0
    while arr[i] != V:
        i += 1
    return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())  # Read the target value

    n = int(input().strip())  # Read the size of the array

    arr = list(map(int, input().rstrip().split()))  # Read the array

    result = introTutorial(V, arr)  # Get the index of V

    fptr.write(str(result) + '\n')  # Write result to output

    fptr.close()