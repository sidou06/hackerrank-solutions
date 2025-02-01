#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'hackerlandRadioTransmitters' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k

def hackerlandRadioTransmitters(x, k):
    # Sort the array of locations to simplify the selection process
    x.sort()
    i = 0
    ant = 0
    # Iterate through all locations in x
    while i < len(x):
        # Start with the first uncovered location
        start = x[i]
        # Find the farthest location within range of the first transmitter
        while i < len(x) and x[i] <= start + k:
            i += 1
        i -= 1
        # Set the medium location where the transmitter will be placed
        medium = x[i]
        ant += 1
        # Move past all locations covered by the current transmitter
        while i < len(x) and x[i] <= medium + k:
            i += 1
    return ant

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()