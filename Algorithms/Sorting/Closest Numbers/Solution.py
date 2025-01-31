#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Sort the array
    arr.sort() 
    
    # Initialize the smallest difference
    diff = max(arr) - min(arr) + 1
    
    # Initialize the result list
    res = []
    
    # Compare consecutive elements to find the closest numbers
    for i in range(1, len(arr)):
        # If a smaller difference is found, update the result list and the smallest difference
        if arr[i] - arr[i - 1] < diff:
            res = [arr[i - 1], arr[i]]
            diff = arr[i] - arr[i - 1] 
        # If the same smallest difference is found, add the pair to the result list
        elif arr[i] - arr[i - 1] == diff:
            res.append(arr[i - 1])
            res.append(arr[i])
    
    return res 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()