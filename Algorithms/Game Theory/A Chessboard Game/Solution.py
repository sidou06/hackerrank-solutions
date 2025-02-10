#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chessboardGame' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x (row position of the piece)
#  2. INTEGER y (column position of the piece)
#

# Initialize a 15x15 chessboard with False values
chess = [[False for _ in range(15)] for _ in range(15)]

# Precompute winning and losing positions
for s in range(29):
    for i in range(max(0, s - 14), min(s, 14) + 1):
        j = s - i
        # Check all valid moves and determine winning positions
        if (i - 2 >= 0 and j + 1 < 15 and chess[i - 2][j + 1] == False):
            chess[i][j] = True
        if (i - 2 >= 0 and j - 1 >= 0 and chess[i - 2][j - 1] == False):
            chess[i][j] = True
        if (i + 1 < 15 and j - 2 >= 0 and chess[i + 1][j - 2] == False):
            chess[i][j] = True
        if (i - 1 >= 0 and j - 2 >= 0 and chess[i - 1][j - 2] == False):
            chess[i][j] = True

def chessboardGame(x, y):
    # Check precomputed result to determine the winner
    if chess[x - 1][y - 1]:
        return "First"  # Player 1 wins
    else:
        return "Second"  # Player 2 wins

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        # Read x and y coordinates
        first_multiple_input = input().rstrip().split()
        x = int(first_multiple_input[0])
        y = int(first_multiple_input[1])

        # Compute the result
        result = chessboardGame(x, y)

        # Write result to output
        fptr.write(result + '\n')

    fptr.close()