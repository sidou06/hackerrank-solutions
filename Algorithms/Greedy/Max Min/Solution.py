#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr.sort()  # Sort the array in ascending order
    diff = []  # Initialize an empty list to store differences
    for i in range(1,len(arr)):  # Iterate through the array
        diff.append(arr[i] - arr[i - 1])  # Calculate the difference between consecutive elements
    big = sum(diff[:k - 1])  # Initialize big with the sum of the first k-1 differences
    act = big  # Set the initial 'act' value to 'big'
    for i in range(len(diff) - k + 1):  # Loop to calculate the smallest range for any k contiguous elements
        act = act - diff[i] + diff[i + k - 1]  # Update the 'act' value by adjusting the range
        if act < big:  # If a smaller range is found, update 'big'
            big = act
    return big  # Return the smallest difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read the number of elements in the array

    k = int(input().strip())  # Read the value of k

    arr = []  # Initialize the array

    for _ in range(n):  # Read the elements of the array
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)  # Call the function to get the result

    fptr.write(str(result) + '\n')  # Write the result to the output

    fptr.close()  # Close the output file