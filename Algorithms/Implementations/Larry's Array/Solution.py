#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    # Initialize the inversion count
    inv = 0
    
    # Count the number of inversions in the array
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                inv += 1  # Increment inversion count when A[i] > A[j]
    
    # If the number of inversions is even, the array can be sorted
    if inv % 2 == 0:
        return "YES"  # Array can be sorted by rotation
    return "NO"  # Array cannot be sorted by rotation

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        n = int(input().strip())  # Read the size of the array

        A = list(map(int, input().rstrip().split()))  # Read the array

        result = larrysArray(A)  # Call the function to check if the array can be sorted

        fptr.write(result + '\n')  # Write the result to output

    fptr.close()