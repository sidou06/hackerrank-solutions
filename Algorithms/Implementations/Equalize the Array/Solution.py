#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Initialize the minimum and maximum values of the array
    mini = min(arr) 
    maxi = max(arr) 
    
    # Create a list to store the count of each element
    nbs = [0 for i in range(mini, maxi + 1)]
    
    # Count the occurrences of each element in the array
    for i in range(len(arr)):
        nbs[arr[i] - mini] += 1 
    
    # The result is the total length of the array minus the highest frequency
    return len(arr) - max(nbs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the size of the array
    n = int(input().strip())

    # Read the array of integers
    arr = list(map(int, input().rstrip().split()))

    # Call the equalizeArray function
    result = equalizeArray(arr)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()