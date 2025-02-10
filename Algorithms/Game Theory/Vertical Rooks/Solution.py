#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'verticalRooks' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY r1
#  2. INTEGER_ARRAY r2
#

def verticalRooks(r1, r2):
    # Initialize an empty list to store the differences
    diff = []
    # Initialize the result variable to 0
    res = 0
    # Loop over the length of the arrays
    for i in range(len(r1)):
        # Calculate the absolute difference between the two corresponding elements and subtract 1
        diff.append(abs(r1[i] - r2[i]) - 1)
    # Loop over the difference list
    for i in range(len(diff)):
        # Perform an XOR operation between the result and the current difference
        res ^= diff[i]
    # If the result is 0, player-1 wins, otherwise player-2 wins
    if res == 0:
        return "player-1"
    return "player-2"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Number of test cases
    t = int(input().strip())

    # Iterate over each test case
    for t_itr in range(t):
        # Number of elements in each array
        n = int(input().strip())

        r1 = []
        # Read the first array
        for _ in range(n):
            r1_item = int(input().strip())
            r1.append(r1_item)

        r2 = []
        # Read the second array
        for _ in range(n):
            r2_item = int(input().strip())
            r2.append(r2_item)

        # Get the result of the game
        result = verticalRooks(r1, r2)

        # Write the result to the output
        fptr.write(result + '\n')

    # Close the output file
    fptr.close()