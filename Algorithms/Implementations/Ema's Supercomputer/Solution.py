#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    # Initialize an empty list to store potential plus sizes and positions
    li = list() 
    
    # Iterate over the entire grid to find potential pluses
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "G":  # If the current cell is "G"
                le = 1  # Initial size of the plus
                # Check the maximum size the plus can have (based on distance from the borders)
                for k in range(min(i, j, len(grid) - i - 1, len(grid[0]) - j - 1)):
                    if grid[i - k - 1][j] == grid[i + k + 1][j] == grid[i][j - k - 1] == grid[i][j + k + 1] == "G":
                        le += 1  # Increase the size of the plus if conditions hold
                # Add the plus (i, j) coordinates and size to the list
                for x in range(1, le + 1):
                    li.append([i, j, x])
    
    # Sort the list of pluses by size in descending order
    l = sorted(li, key=lambda x: x[2], reverse=True)
    
    ma = 0  # Initialize the maximum area
    # Iterate through all possible pairs of pluses to check if they don't overlap
    for i in range(len(l) - 1):
        f1 = l[i]
        i1, j1, l1 = f1[0], f1[1], f1[2]
        
        # If the area of the first plus is already smaller than the current max, break early
        if (4 * (l1 - 1) + 1) ** 2 <= ma:
            break
        
        # Get the coordinates of the cells covered by the first plus
        c1 = [[i1, j1]]
        for k in range(l1 - 1):
            c1.append([i1 + k + 1, j1])
            c1.append([i1 - k - 1, j1])
            c1.append([i1, j1 + k + 1])
            c1.append([i1, j1 - k - 1])
        
        # Iterate through the remaining pluses to check for non-overlapping pairs
        for j in range(i + 1, len(l)):
            f2 = l[j]
            i2, j2, l2 = f2[0], f2[1], f2[2]
            
            # If the area of the product of the two pluses is smaller than the current max, break early
            if (4 * (l1 - 1) + 1) * (4 * (l2 - 1) + 1) <= ma:
                break
            
            # Get the coordinates of the cells covered by the second plus
            c2 = [[i2, j2]]
            for k in range(l2 - 1):
                c2.append([i2 + k + 1, j2])
                c2.append([i2 - k - 1, j2])
                c2.append([i2, j2 + k + 1])
                c2.append([i2, j2 - k - 1])
            
            # If the two pluses don't overlap, calculate the area and update the maximum area
            if len([c for c in c1 if c in c2]) == 0:
                ma = (4 * (l1 - 1) + 1) * (4 * (l2 - 1) + 1)
    
    # Return the maximum area found
    return ma 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the grid dimensions (n, m) and the grid itself
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    grid = []

    # Read the grid data
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    # Get the result from twoPluses function
    result = twoPluses(grid)

    # Write the result to output
    fptr.write(str(result) + '\n')

    fptr.close()