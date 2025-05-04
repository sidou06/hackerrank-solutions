#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts INTEGER_ARRAY balls as parameter.
#

def solve(balls):
    # Calculate and return half of the sum of all ball values
    return sum(balls) / 2

if __name__ == '__main__':
    # Open the output file using the path specified in environment variables
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of balls
    balls_count = int(input().strip())

    # Initialize the list of balls
    balls = []

    # Read each ball value from input
    for _ in range(balls_count):
        balls_item = int(input().strip())
        balls.append(balls_item)

    # Call the solve function to get the result
    result = solve(balls)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()