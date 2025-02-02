#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    # Write your code here
    i = 0
    tot = 0
    while i < len(arr):
        j = min(i + k - 1, len(arr) - 1)
        stop = max(0,i - k + 1)
        while j >= stop:
            if arr[j] == 1:
                i = j + k
                tot += 1
                break
            else:
                j -= 1
        if j < stop:
            return(-1)
    return tot
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()