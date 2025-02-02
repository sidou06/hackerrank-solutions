#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Sort each row of the grid alphabetically
    for i in range(len(grid)):
        grid[i] = "".join(sorted(grid[i]))

    # Check if columns are sorted in non-decreasing order
    order = True 
    i = 0
    while i < len(grid[0]) and order:
        j = 0
        while j < len(grid) - 1 and order:
            if grid[j][i] > grid[j + 1][i]:  # Check if the column is not sorted
                order = False 
            j += 1
        i += 1
    
    # Return "YES" if all columns are sorted, otherwise return "NO"
    return "YES" if order else "NO"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        # Read the size of the grid
        n = int(input().strip())

        grid = []

        # Read the grid rows
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        # Compute the result
        result = gridChallenge(grid)

        # Write the result to output
        fptr.write(result + '\n')

    fptr.close()