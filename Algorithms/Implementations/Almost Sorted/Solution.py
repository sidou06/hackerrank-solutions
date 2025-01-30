#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Initialize the index i for traversing the array
    i = 0
    
    # Find the first element that is greater than the next element
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            break  # Found the point where the array is unsorted
        i += 1
    
    # If no such point is found, the array is already sorted
    if i == len(arr) - 1:
        print("yes")
        return 0
    
    # Identify the largest element and its index for swapping
    big = arr[i]
    ind = arr.index(min(arr[i + 1:]))  # Find the smallest element in the unsorted part
    smal = arr[ind]
    
    # Try swapping the identified elements
    arr[ind] = big
    arr[i] = smal
    
    # Check if the array is sorted after the swap
    if arr == sorted(arr):
        print("yes")
        print("swap", i + 1, ind + 1)  # Print 1-based indices for the swap
        return 0
    
    # Undo the swap to try another operation
    arr[ind] = smal
    arr[i] = big
    
    # Find the end index of the decreasing subsequence for reversing
    j = i + 1
    while j < len(arr) and arr[j] <= arr[j - 1]:
        j += 1
    
    # Reverse the decreasing subsequence and check if the array becomes sorted
    arr[i:j] = list(reversed(arr[i:j]))
    if arr == sorted(arr):
        print("yes")
        print("reverse", i + 1, j)  # Print 1-based indices for the reverse
        return 0
    
    # If no operation results in a sorted array, print "no"
    print("no")
    return 0

if __name__ == '__main__':
    n = int(input().strip())  # Read the size of the array

    arr = list(map(int, input().rstrip().split()))  # Read the array

    almostSorted(arr)  # Call the function to determine the operation