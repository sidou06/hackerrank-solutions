#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sansaXor(arr):
    # If the array length is even, the XOR of all subarrays will be 0
    if len(arr) % 2 == 0:
        return 0
    # Initialize result variable
    res = 0
    # Iterate through the array and XOR every second element
    for i in range(0, len(arr), 2):
        res ^= arr[i]
    return res  # Return the final XOR value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        n = int(input().strip())  # Read the length of the array

        arr = list(map(int, input().rstrip().split()))  # Read the array of integers

        result = sansaXor(arr)  # Compute the result

        fptr.write(str(result) + '\n')  # Write the result to output

    fptr.close()