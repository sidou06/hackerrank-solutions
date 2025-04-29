#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumOfGroup' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER k as parameter.
#

def sumOfGroup(k):
    # First element of the k-th group:
    # The sequence is formed of groups of odd numbers where:
    # Group 1: 1
    # Group 2: 3, 5
    # Group 3: 7, 9, 11
    # Group 4: 13, 15, 17, 19, ...
    # The first element of the k-th group = 1 + sum of (2*i - 1) for i from 1 to k-1
    # That sum = k*(k - 1), then add 1 to get the actual first number
    p = (k * (k - 1)) + 1  # First number in the k-th group

    # Use arithmetic progression sum formula:
    # Sum = n/2 * (first_term + last_term)
    # Number of terms in the group = k
    # Last term = p + 2*(k - 1)
    s = (k * (p + p + 2 * (k - 1))) // 2  # Sum of k odd numbers starting from p

    return s  # Return the computed sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file

    k = int(input().strip())  # Read the group number

    answer = sumOfGroup(k)  # Compute the sum for the k-th group

    fptr.write(str(answer) + '\n')  # Write the result to the output file

    fptr.close()  # Close the file