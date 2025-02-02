#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestIncreasingSubsequence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from bisect import bisect_left

def longestIncreasingSubsequence(arr):
    # Initialize the result list with the first element of the array
    res = [arr[0]]  
    # Loop through the remaining elements of the array
    for i in range(1,len(arr)):
        # If the current element is larger than or equal to the last element in the result list, append it
        if arr[i] >= res[-1]:
            res.append(arr[i])
        else:
            # Otherwise, find the correct position using binary search and replace the element at that position
            pos = bisect_left(res, arr[i])
            res[pos] = arr[i]
    # Return the length of the result list, which represents the length of the longest increasing subsequence
    return len(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Input the size of the array
    n = int(input().strip())

    arr = []

    # Input the array elements
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    # Get the length of the longest increasing subsequence
    result = longestIncreasingSubsequence(arr)

    # Write the result to the output
    fptr.write(str(result) + '\n')

    fptr.close()