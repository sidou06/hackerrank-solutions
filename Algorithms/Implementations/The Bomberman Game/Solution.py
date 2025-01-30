#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Initialize an empty list to store the states
    states = []
    
    # If n == 1, just return the original grid since no bombs explode
    if n == 1:
        return grid
    
    # Create a grid where all cells are bombs (full grid)
    full = ["O" * len(grid[0])] * len(grid)
    
    # If n is even, all cells will be bombs at the end, return the full grid
    if n % 2 == 0:
        return full
    
    # Simulation for odd values of n (only need 2 states: after 1st and 2nd explosion)
    for i in range(2):
        # Create an empty grid for the alternate state
        alter = ["O" * len(grid[0])] * len(grid)
        
        # Loop through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "O":  # Bomb found, it will explode
                    # Set the current cell to '.' (empty after explosion)
                    alter[i] = alter[i][:j] + "." + alter[i][j + 1:]
                    # Set adjacent cells to '.' as well (they are affected by the bomb)
                    if i > 0:
                        alter[i - 1] = alter[i - 1][:j] + "." + alter[i - 1][j + 1:]
                    if i < len(grid) - 1:
                        alter[i + 1] = alter[i + 1][:j] + "." + alter[i + 1][j + 1:]
                    if j > 0:
                        alter[i] = alter[i][:j - 1] + "." + alter[i][j:]
                    if j < len(grid[0]) - 1:
                        alter[i] = alter[i][:j + 1] + "." + alter[i][j + 2:]
        
        # Append the altered state to the states list
        states.append(alter)
        # Set grid to the altered state for the next round
        grid = alter
    
    # If n % 4 == 1, return the second state (after 2 explosions)
    if n % 4 == 1:
        return states[1]
    
    # Otherwise, return the first state (after 1 explosion)
    return states[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the grid dimensions and the number of seconds
    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    n = int(first_multiple_input[2])

    # Read the grid
    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    # Get the result from bomberMan function
    result = bomberMan(n, grid)

    # Write the result to output
    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()