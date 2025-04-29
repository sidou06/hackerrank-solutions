#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'solve' function below
# The function returns an INTEGER
# The function accepts 2D_INTEGER_ARRAY steps as parameter
def solve(steps):
    # Initialize minx and miny with the first step coordinates
    minx = steps[0][0]
    miny = steps[0][1]
    
    # Get the number of steps
    val = len(steps)
    
    # Iterate through all steps
    for i in range(val):
        # Update minx if current x is smaller
        if steps[i][0] < minx:
            minx = steps[i][0]
        # Update miny if current y is smaller
        if steps[i][1] < miny:
            miny = steps[i][1]
    
    # Return the area formed by the minimum x and y
    return minx * miny

# Entry point of the program
if __name__ == '__main__':
    # Open the output file
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of steps
    n = int(input().strip())

    # Initialize list to store steps
    steps = []

    # Read each step and add it to the list
    for _ in range(n):
        steps.append(list(map(int, input().rstrip().split())))

    # Call solve function and get the result
    result = solve(steps)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()