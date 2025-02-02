#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    # Initialize an array to store candies count, each child gets at least 1
    candies = [1] * n

    # Forward pass to ensure right neighbor gets more candies if they have a higher rating
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Backward pass to ensure left neighbor gets more candies if they have a higher rating
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    # Return the total candies required
    return sum(candies)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of children
    n = int(input().strip())

    # Read the ratings of each child
    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    # Compute the minimum number of candies needed
    result = candies(n, arr)

    # Write the result to output
    fptr.write(str(result) + '\n')

    fptr.close()