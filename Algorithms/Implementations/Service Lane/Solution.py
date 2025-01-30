#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(n, cases):
    # Create an empty list to store the results for each test case
    final = []
    
    # Loop through each case in the cases list
    for case in cases:
        # Slice the width array from the start to the end index given in the case
        part = width[case[0]:case[1] + 1]
        # Find the minimum value in the sliced part of the array and append it to the final result list
        final.append(min(part))
    
    return final  # Return the list of results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the first line input containing n (number of lanes) and t (number of test cases)
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])  # Number of lanes
    t = int(first_multiple_input[1])  # Number of test cases

    # Read the width of the lanes
    width = list(map(int, input().rstrip().split()))

    cases = []

    # Read each test case
    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    # Call the function with the inputs and get the results
    result = serviceLane(n, cases)

    # Write the result to the output file, with each result on a new line
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()