#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'connectedCell' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.

def connectedCell(matrix):
    # Initialize lists to track cells already processed and regions found
    done = []
    regions = []
    n = len(matrix)  # Get the number of rows in the matrix
    m = len(matrix[0])  # Get the number of columns in the matrix

    # Iterate through all the cells in the matrix
    for i in range(n):
        for j in range(m):
            # If the current cell has a value of 1, it's part of a region
            if matrix[i][j] == 1:
                # Encode the position of the cell as a unique value (i*10 + j)
                value = 10 * i + j
                # If this cell has not been processed already
                if value not in done:
                    done.append(value)  # Mark the cell as processed
                    new_region = [value]  # Create a new region list and add the starting cell
                    current_try = [value]  # Initialize a list for cells to explore

                    # Process the cells in the current region
                    while len(current_try):
                        value = current_try[0]  # Get the current cell to explore
                        x = value // 10  # Extract the row index from the unique value
                        y = value % 10  # Extract the column index from the unique value
                        
                        # Check and add the top-left neighbor (if valid) to the current region
                        if x > 0 and y > 0 and matrix[x - 1][y - 1] and (((x - 1) * 10 + y - 1) not in new_region):
                            new = (x - 1) * 10 + y - 1  # Encode the new cell position
                            new_region.append(new)  # Add the neighbor to the region
                            done.append(new)  # Mark the neighbor as processed
                            current_try.append(new)  # Add the neighbor to explore later
            
                        # Check and add the top neighbor (if valid) to the current region
                        if x > 0 and matrix[x - 1][y] and (((x - 1) * 10 + y) not in new_region):
                            new = (x - 1) * 10 + y
                            new_region.append(new)
                            done.append(new)
                            current_try.append(new)
                        
                        # Check and add the top-right neighbor (if valid) to the current region
                        if x > 0 and y < m - 1 and matrix[x - 1][y + 1] and (((x - 1) * 10 + y + 1)) not in new_region:
                            new = (x - 1) * 10 + y + 1
                            new_region.append(new)
                            done.append(new)
                            current_try.append(new)

                        # Check and add the left neighbor (if valid) to the current region
                        if y > 0 and matrix[x][y - 1] and ((x * 10 + y - 1) not in new_region):
                            new = x * 10 + y - 1
                            new_region.append(new)
                            done.append(new)
                            current_try.append(new)
                        
                        # Check and add the right neighbor (if valid) to the current region
                        if y < m - 1 and matrix[x][y + 1] and ((x * 10 + y + 1) not in new_region):
                            new = x * 10 + y + 1
                            new_region.append(new)
                            done.append(new)
                            current_try.append(new)

                        # Check and add the bottom-left neighbor (if valid) to the current region
                        if x < n - 1 and y > 0 and matrix[x + 1][y - 1] and (((x + 1) * 10 + y - 1) not in new_region):
                            new = (x + 1) * 10 + y - 1
                            new_region.append(new)
                            done.append(new)
                            current_try.append(new)

                        # Check and add the bottom neighbor (if valid) to the current region
                        if x < n - 1 and matrix[x + 1][y] and (((x + 1) * 10 + y) not in new_region):
                            new = (x + 1) * 10 + y
                            new_region.append(new)
                            done.append(new)
                            current_try.append(new)

                        # Check and add the bottom-right neighbor (if valid) to the current region
                        if x < n - 1 and y < m - 1 and matrix[x + 1][y + 1] and (((x + 1) * 10 + y + 1)) not in new_region:
                            new = (x + 1) * 10 + y + 1
                            new_region.append(new)
                            done.append(new)
                            current_try.append(new)
                        
                        # Remove the processed cell from the list of cells to explore
                        current_try = current_try[1:]

                    # Append the discovered region to the list of regions
                    regions.append(new_region)

    # Find the largest region by its length
    l = max([len(x) for x in regions])
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read the number of rows in the matrix

    m = int(input().strip())  # Read the number of columns in the matrix

    matrix = []

    # Read the matrix rows
    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)  # Get the largest connected region size

    fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()