#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Initialize the variable to store the minimum distance
    di = len(a)
    
    # Loop through each element in the array
    for i in range(len(a) - 1):
        # Start comparing with the next element
        j = i + 1 
        
        # Keep moving 'j' until we find a match
        while j < len(a) and a[i] != a[j]:
            j = j + 1
        
        # If we find a match and the distance is smaller than the current minimum, update it
        if j != len(a) and j - i < di:
            di = j - i
    
    # If no match was found, set distance to -1
    if di == len(a):
        di = -1
    
    # Return the minimum distance
    return di

if __name__ == '__main__':
    # Open the output file for writing the result
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of elements in the array
    n = int(input().strip())

    # Read the array of integers
    a = list(map(int, input().rstrip().split()))

    # Call the function to find the minimum distance
    result = minimumDistances(a)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()