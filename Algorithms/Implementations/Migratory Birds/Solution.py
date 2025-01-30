#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Sort the array to group similar birds together
    arr.sort()
    
    best = cpt = 0
    cu = arr[0]
    
    # Iterate through the array and count occurrences of each bird type
    for i in range(len(arr)):
        if arr[i] == cu:
            cpt += 1
        else:
            # Update the result when a new bird type is found
            if cpt > best:
                ans = arr[i - 1]
                best = cpt
            cpt = 1
            cu = arr[i]
    
    # In case the most frequent bird is at the end
    if cpt > best:
        ans = arr[-1]
    
    return ans    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    # Get the result and write it to the output file
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')

    fptr.close()