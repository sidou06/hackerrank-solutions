#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Initialize an empty list to store the result
    res = []
    
    # Get the size of the grid (assuming it's square)
    n = len(grid)
    
    # Iterate through each row in the grid
    for i in range(n):
        row = ''  # Initialize an empty string to construct the row with potential changes
        # Iterate through each column in the current row
        for j in range(n):
            # Check if the current element is on the boundary (first or last row/column)
            if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                row += grid[i][j]  # Keep the element as is if it's on the boundary
            # Check if the current element is greater than its neighboring elements
            elif int(grid[i][j]) > max(int(grid[i][j - 1]), int(grid[i][j + 1]), int(grid[i - 1][j]), int(grid[i + 1][j])):
                row += 'X'  # Replace the element with 'X' if it's a cavity (greater than neighbors)
            else:
                row += grid[i][j]  # Keep the element as is if it's not a cavity
        res.append(row)  # Add the modified row to the result list
    
    # Return the list of modified rows
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the size of the grid
    n = int(input().strip())

    grid = []

    # Read the grid from input
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    # Call the function to get the modified grid
    result = cavityMap(grid)

    # Write the result to the output file
    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()