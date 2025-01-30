#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Initialize the number of valleys and the current level
    valleys = 0
    level = 0

    # Iterate through the path
    for i in range(steps):
        # Check for a valley when the level is 0 and the step is 'D'
        if level == 0 and path[i] == 'D':
            valleys += 1

        # Update the level based on the step ('D' or 'U')
        if path[i] == 'D':
            level -= 1
        else:
            level += 1    

    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())  # Total number of steps

    path = input()  # The sequence of steps (U or D)

    result = countingValleys(steps, path)  # Calculate the number of valleys

    fptr.write(str(result) + '\n')

    fptr.close()