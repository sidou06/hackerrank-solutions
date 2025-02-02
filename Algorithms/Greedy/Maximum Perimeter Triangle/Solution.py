#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Sort the sticks in ascending order
    sticks.sort() 

    # Iterate while there are at least three sticks left
    while len(sticks) > 2:
        # Check if the last three sticks can form a valid triangle
        if sticks[-1] >= sticks[-2] + sticks[-3]:
            sticks.pop(-1)  # Remove the largest stick if it cannot form a triangle
        else:
            return sticks[-3:]  # Return the largest valid triangle found

    # If no valid triangle is found, return [-1]
    return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of sticks
    n = int(input().strip())

    # Read the stick lengths
    sticks = list(map(int, input().rstrip().split()))

    # Compute the result
    result = maximumPerimeterTriangle(sticks)

    # Write the result to output
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()