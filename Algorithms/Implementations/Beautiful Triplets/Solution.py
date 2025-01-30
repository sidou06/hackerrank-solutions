#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Initialize the variable to store the count of triplets
    tot = 0
    # Create a list to store the counts of elements at different differences
    rep = [0 for i in range(max(arr) - min(arr) + 1)]
    
    # Loop through the array and update the counts in the 'rep' list
    for i in range(len(arr)):
        rep[arr[i] - arr[0]] += 1
    
    # Loop through the 'rep' list to count all possible triplets with the given difference 'd'
    for i in range(len(rep) - 2 * d):
        tot += rep[i] * rep[i + d] * rep[i + 2 * d]
    
    # Return the total count of beautiful triplets
    return tot
        
if __name__ == '__main__':
    # Open the output file for writing the result
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the first line of input (number of elements and the difference d)
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    # Read the array of numbers
    arr = list(map(int, input().rstrip().split()))

    # Call the function to find the number of beautiful triplets
    result = beautifulTriplets(d, arr)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()