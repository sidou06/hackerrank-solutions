#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Initialize the result list with the initial length of the array
    res = [len(arr)]
    
    # Continue until the array is empty
    while len(arr) > 0:
        # Find the minimum element in the array
        m = min(arr)
        
        # Iterate over the array and remove all instances of the minimum element
        i = 0
        while i < len(arr):
            if arr[i] == m:
                del(arr[i])
            else:
                i += 1
                
        # Append the current length of the array after removing elements
        res.append(len(arr))
    
    # Return the result without the last length (as no sticks will be cut after the last operation)
    return res[:-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the size of the array
    n = int(input().strip())

    # Read the array elements
    arr = list(map(int, input().rstrip().split()))

    # Call the cutTheSticks function to get the result
    result = cutTheSticks(arr)

    # Write the result to the output file
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    # Close the output file
    fptr.close()