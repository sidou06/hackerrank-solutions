#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Initialize maximum sum to the lowest possible hourglass sum (-9 * 7 = -63)
    cu = -63
    # Iterate over possible top-left positions of hourglasses
    for i in range(4):
        for j in range(4):
            # Calculate the hourglass sum
            hug = sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j + 3]) 
            # Update the maximum hourglass sum if the current sum is greater
            if hug > cu: 
                cu = hug 
    return cu 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the 6x6 2D array
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # Compute the maximum hourglass sum
    result = hourglassSum(arr)

    # Write the result to output
    fptr.write(str(result) + '\n')

    fptr.close()