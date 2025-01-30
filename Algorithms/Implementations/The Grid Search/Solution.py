#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    # Get the number of rows and columns for both G and P
    R = len(G)
    C = len(G[0])
    r = len(P)
    c = len(P[0])
    
    # Variable to track if a match is found
    corr = False
    
    # Start iterating through the main grid G
    i = 0
    while (i <= R - r and not corr):
        j = 0
        while(j <= C - c and not corr):
            corr = True  # Assume a match is found initially
            pi = pj = 0
            gi = i
            gj = j
            while(pi < r and corr):  # Iterate through the pattern grid P
                # Compare the elements of G and P
                if(G[gi][gj] != P[pi][pj]):
                    corr = False  # Set to False if mismatch found
                pj += 1  # Move to the next column in P
                gj += 1  # Move to the next column in G
                if (pj == c):  # If the pattern column is complete, reset
                    pj = 0
                    gj = j
                    pi += 1  # Move to the next row in P
                    gi += 1  # Move to the next row in G
            j += 1  # Move to the next column in G
        i += 1  # Move to the next row in G
    
    # If a match is found, return 'YES', else return 'NO'
    if corr:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        # Read the dimensions of the grid G
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])
        C = int(first_multiple_input[1])

        G = []

        # Read the rows of grid G
        for _ in range(R):
            G_item = input()
            G.append(G_item)

        # Read the dimensions of the pattern P
        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])
        c = int(second_multiple_input[1])

        P = []

        # Read the rows of pattern P
        for _ in range(r):
            P_item = input()
            P.append(P_item)

        # Call gridSearch function and write the result
        result = gridSearch(G, P)
        fptr.write(result + '\n')

    fptr.close()