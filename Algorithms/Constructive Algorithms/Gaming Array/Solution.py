#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    # Initialize index and count of turns
    i = 0
    count = 1  # Starts with Bob's turn
    
    # Find the maximum element in the array
    m = max(arr)
    
    # Track the highest encountered value
    highest = arr[0]
    
    # Iterate through the array to count the number of turns
    while i < len(arr) and highest != m:
        if arr[i] > highest:
            highest = arr[i]
            count += 1  # Each new max value represents a new turn
        i += 1
    
    # If count is odd, Bob wins; otherwise, Andy wins
    if count % 2:
        return "BOB"
    return "ANDY"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    g = int(input().strip())

    for g_itr in range(g):
        # Read the number of elements in the array
        arr_count = int(input().strip())

        # Read the array elements
        arr = list(map(int, input().rstrip().split()))

        # Determine the winner
        result = gamingArray(arr)

        # Write the result to the output
        fptr.write(result + '\n')

    fptr.close()