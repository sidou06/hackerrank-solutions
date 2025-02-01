#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'printShortestPath' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER i_start
#  3. INTEGER j_start
#  4. INTEGER i_end
#  5. INTEGER j_end
#

def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Calculate the differences in row (i) and column (j) positions
    i = i_start - i_end
    j = j_start - j_end

    # Check if the move is impossible based on the row and column differences
    if i % 2 or ((j - i // 2) % 2):
        print("Impossible")
        return

    # Initialize an empty list to store the path
    path = []

    # First loop: move diagonally upwards-left (UL) while both i > 0 and i // 2 + j > 0
    while i > 0 and i // 2 + j > 0:
        path.append("UL")  # Append "UL" to the path
        i -= 2  # Decrease the row difference by 2
        j -= 1  # Decrease the column difference by 1

    # Second loop: move diagonally upwards-right (UR) while i > 0
    while i > 0:
        path.append("UR")  # Append "UR" to the path
        i -= 2  # Decrease the row difference by 2
        j += 1  # Increase the column difference by 1

    # Third loop: move right (R) while j < 0 and j < i // 2
    while j < 0 and j < i // 2:
        path.append("R")  # Append "R" to the path
        j += 2  # Increase the column difference by 2

    # Fourth loop: move diagonally left-right (LR) while i < 0 and 0 > j + (i // 2)
    while i < 0 and 0 > j + (i // 2):
        path.append("LR")  # Append "LR" to the path
        i += 2  # Increase the row difference by 2
        j += 1  # Increase the column difference by 1

    # Fifth loop: move diagonally left-left (LL) while i < 0
    while i < 0:
        path.append("LL")  # Append "LL" to the path
        i += 2  # Increase the row difference by 2
        j -= 1  # Decrease the column difference by 1

    # Sixth loop: move left (L) while j > 0
    while j > 0:
        path.append("L")  # Append "L" to the path
        j -= 2  # Decrease the column difference by 2

    # Print the length of the path and the sequence of moves
    print(len(path))
    print(" ".join(x for x in path))
    return
    
            
if __name__ == '__main__':
    n = int(input().strip())  # Read the input for n

    # Read the starting and ending coordinates
    first_multiple_input = input().rstrip().split()
    i_start = int(first_multiple_input[0])
    j_start = int(first_multiple_input[1])
    i_end = int(first_multiple_input[2])
    j_end = int(first_multiple_input[3])

    # Call the printShortestPath function with the provided inputs
    printShortestPath(n, i_start, j_start, i_end, j_end)