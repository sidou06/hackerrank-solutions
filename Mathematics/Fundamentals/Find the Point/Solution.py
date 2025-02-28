#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findPoint' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER px
#  2. INTEGER py
#  3. INTEGER qx
#  4. INTEGER qy
#

def findPoint(px, py, qx, qy):
    # Write your code here
    
    # List to store the coordinates of the reflection point
    R = []
    
    # Compute the x-coordinate of the reflection point
    R.append(px + 2*(qx-px))
    
    # Compute the y-coordinate of the reflection point
    R.append(py + 2*(qy-py))
    
    # Return the coordinates of the reflection point
    return R
    
if __name__ == '__main__':
    # Open the output file
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    n = int(input().strip())

    for n_itr in range(n):
        # Read input values and split them into individual integers
        first_multiple_input = input().rstrip().split()

        px = int(first_multiple_input[0])
        py = int(first_multiple_input[1])
        qx = int(first_multiple_input[2])
        qy = int(first_multiple_input[3])

        # Call the function to find the reflection point
        result = findPoint(px, py, qx, qy)

        # Write the result to the output file
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    # Close the output file
    fptr.close()