#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Initialize height and width of the grid
    h = len(A) 
    w = len(A[0])
    
    # Initial surface area is the sum of the top and bottom surfaces of all cells
    som = 2 * h * w
    
    # Add the surface area of the leftmost and rightmost vertical sides
    for i in range(h):
        som += A[i][0] + A[i][w - 1]
    
    # Add the surface area of the topmost and bottommost horizontal sides
    for j in range(w):
        som += A[0][j] + A[h - 1][j]
    
    # Add the surface area for the differences between adjacent cells vertically
    for i in range(1, h):
        for j in range(w):
            som += abs(A[i][j] - A[i - 1][j])
    
    # Add the surface area for the differences between adjacent cells horizontally
    for j in range(1, w):
        for i in range(h):
            som += abs(A[i][j] - A[i][j - 1])
    
    return som  # Return the total surface area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the dimensions of the grid (height and width)
    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])
    W = int(first_multiple_input[1])

    A = []

    # Read the grid values
    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    # Call the function and get the surface area
    result = surfaceArea(A)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    fptr.close()