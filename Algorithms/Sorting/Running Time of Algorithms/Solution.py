#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    # Count the number of shifts
    shifts = 0
    
    # Iterate over the array starting from index 1
    for i in range(1, len(arr)):
        pos = i 
        
        # Find the correct position for arr[i]
        while pos > 0 and arr[i] < arr[pos - 1]:
            shifts += 1
            pos -= 1
        
        # Store the current value
        save = arr[i]
        
        # Shift elements to make space
        for j in range(i, pos, -1):
            arr[j] = arr[j - 1]
        
        # Place the value in its correct position
        arr[pos] = save
    
    return shifts 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()