#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY operations as parameter.
#

def solve(operations, n):
    # Initialize rotation flag
    rot = False
    
    # Initialize position offset
    pos = 0
    
    # Iterate through each operation
    for i in range(len(operations)):
        if operations[i][0] == 1:
            # Type 1 operation: Shift the position forward by given value
            pos += operations[i][1]
            pos %= n  # Ensure it wraps around using modulo
        else:
            # Type 2 operation: Flip the orientation
            rot = not rot  # Toggle rotation flag
            # Recalculate the new reference position after flip
            pos = operations[i][1] - pos
            pos %= n  # Again, ensure wrap-around

    # Construct the result based on the final orientation
    if rot:
        # If the final state is flipped, return type 2 and current position
        res = [2, pos]
    else:
        # Otherwise, return type 1 and adjusted position
        res = [1, n - pos]
    
    return res

if __name__ == '__main__':
    # Open output file
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read n and m (number of elements and number of operations)
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    operations = []

    # Read all operations
    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))

    # Solve and get result
    result = solve(operations, n)

    # Write result to output
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
