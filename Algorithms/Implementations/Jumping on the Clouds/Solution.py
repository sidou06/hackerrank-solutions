#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Initialize current position and the jump counter
    current = 0
    jumps = 0
    
    # Continue jumping until reaching the last cloud
    while current < len(c) - 1:
        # Check if we can make a jump of 2 clouds (if not on a thundercloud)
        if current + 2 < len(c) and c[current + 2] == 0:
            current += 2
        else:
            # Otherwise jump to the next cloud
            current += 1
        # Increase the jump count after each jump
        jumps += 1
        
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of clouds (n)
    n = int(input().strip())

    # Read the cloud status array (0 for safe, 1 for thundercloud)
    c = list(map(int, input().rstrip().split()))

    # Call the jumpingOnClouds function
    result = jumpingOnClouds(c)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()