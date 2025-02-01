#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'pairs' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr

def pairs(k, arr):
    # Sort the array to make it easier to find the pairs
    arr.sort() 
    count = 0
    i = 1
    j = 0
    # Use two pointers to find pairs with difference equal to k
    while i < len(arr):
        diff = arr[i] - arr[j]
        if diff == k:
            j += 1
            i += 1
            count += 1
        elif diff < k:
            i += 1
        else:
            j += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()