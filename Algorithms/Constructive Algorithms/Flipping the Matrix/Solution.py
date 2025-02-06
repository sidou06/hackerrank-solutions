#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Initialize the sum of the maximum quadrant
    som = 0
    # Get the size of the matrix
    l = len(matrix)
    
    # Iterate over the top-left quadrant of the matrix
    for i in range(l // 2):
        for j in range(l // 2):
            # Find the maximum value among the four possible reflections
            som += max(matrix[i][j], 
                       matrix[l - i - 1][j], 
                       matrix[i][l - j - 1], 
                       matrix[l - i - 1][l - j - 1])
    
    return som
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    q = int(input().strip())

    for q_itr in range(q):
        # Read the matrix dimension (half of the actual size)
        n = int(input().strip())

        # Initialize the matrix
        matrix = []

        # Read the 2n x 2n matrix
        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        # Compute the maximum sum of the top-left quadrant
        result = flippingMatrix(matrix)

        # Write the result to the output
        fptr.write(str(result) + '\n')

    fptr.close()