#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

# List of all possible 3x3 magic squares
sqs = [
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
]

def formingMagicSquare(s):
    # Initialize the minimum cost with a large number
    m = 100 
    # Compare the input square with each magic square
    for sq in sqs:
        c = 0
        # Calculate the cost to convert the current square into the magic square
        for i in range(3):
            for j in range(3):
                c += abs(sq[i][j] - s[i][j])
        # Update the minimum cost
        if c < m:
            m = c 
    return m 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input 3x3 matrix
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    # Get the result
    result = formingMagicSquare(s)

    # Write the result to the output
    fptr.write(str(result) + '\n')

    fptr.close()