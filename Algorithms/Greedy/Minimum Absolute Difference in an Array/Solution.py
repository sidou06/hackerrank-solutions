#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Sort the array to bring close values next to each other
    arr.sort() 
    
    # Initialize the minimum difference with the first pair
    diff = arr[1] - arr[0]
    
    # Iterate through the array to find the minimum absolute difference
    for i in range (1, len(arr) - 1):
        if arr[i + 1] - arr[i] < diff:
            diff = arr[i + 1] - arr[i]
    
    return diff 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input size
    n = int(input().strip())

    # Read array elements
    arr = list(map(int, input().rstrip().split()))

    # Compute the result
    result = minimumAbsoluteDifference(arr)

    # Write the output
    fptr.write(str(result) + '\n')

    fptr.close()