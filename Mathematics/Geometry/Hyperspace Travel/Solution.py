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
# The function accepts 2D_INTEGER_ARRAY friends as parameter.
#

def solve(friends):
    # Initialize an empty list to store results
    sol = []
    # Get number of rows (n) and columns (m)
    n = len(friends)
    m = len(friends[0])
    
    # Loop through each column (m)
    for i in range(m):
        # Initialize an empty list to store elements of the current column
        line = []
        # Loop through each row (n) and add the elements of the current column to 'line'
        for j in range(n):
            line.append(friends[j][i])
        
        # Sort the elements in the column
        line.sort()
        # Append the median element (middle element after sorting) to 'sol'
        sol.append(line[(len(line) - 1) // 2])
    
    # Return the final list of median values for each column
    return sol

if __name__ == '__main__':
    # Open output file for writing
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values for number of rows (n) and columns (m)
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])  # number of rows
    m = int(first_multiple_input[1])  # number of columns

    # Initialize the list of friends (2D array)
    friends = []

    # Read the 2D array from input
    for _ in range(n):
        friends.append(list(map(int, input().rstrip().split())))

    # Get the result from solve function
    result = solve(friends)

    # Write the result to the output file, with space-separated values
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    # Close the output file
    fptr.close()