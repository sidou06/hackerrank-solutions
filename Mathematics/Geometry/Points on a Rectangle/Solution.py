#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#

def solve(coordinates):
    # Initialize lists to store x and y coordinates separately
    x = []
    y = [] 
    for c in coordinates:
        # Append x coordinate
        x.append(c[0])
        # Append y coordinate
        y.append(c[1])
    
    # Find minimum x value
    x1 = min(x)
    # Find maximum x value
    x2 = max(x)
    # Find minimum y value
    y1 = min(y) 
    # Find maximum y value
    y2 = max(y) 
    
    for c in coordinates:
        # Check if the point is not on the rectangle border
        if c[0] not in [x1, x2] and c[1] not in [y1, y2]:
            # If not on border, return NO
            return "NO"
    
    # If all points are on the border, return YES
    return "YES"

if __name__ == '__main__':
    # Open output file
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of queries
    q = int(input().strip())

    for q_itr in range(q):
        # Read number of coordinates
        n = int(input().strip())

        # Initialize coordinates list
        coordinates = []

        for _ in range(n):
            # Read each coordinate pair
            coordinates.append(list(map(int, input().rstrip().split())))

        # Get result from solve function
        result = solve(coordinates)

        # Write result to output file
        fptr.write(result + '\n')

    # Close output file
    fptr.close()