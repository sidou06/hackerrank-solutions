#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    # Sort the array in descending order to get the largest permutation
    s = sorted(arr, reverse=True)
    
    # Initialize the index to start comparing the elements
    i = 0 
    
    # Get the length of the array
    l = len(arr) 
    
    # Create a dictionary to store the indices of each element
    indexdict = {val: i for i, val in enumerate(arr)}
    
    # Swap elements to make the largest permutation within k swaps
    while i < l and k > 0:
        # Skip elements that are already in their correct positions
        while i < l and s[i] == arr[i]:
            i += 1
        if i < l:
            # Find the index of the element to swap
            ind = indexdict[s[i]]
            
            # Perform the swap
            arr[ind] = arr[i]
            arr[i] = s[i]
            
            # Update the indices in the dictionary
            indexdict[arr[ind]] = ind
            indexdict[arr[i]] = i
            
            # Decrease the number of remaining swaps
            k -= 1 
            i += 1 
    
    # Return the resulting array after the swaps
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    # Get the result after performing the swaps
    result = largestPermutation(k, arr)

    # Write the result to output
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()