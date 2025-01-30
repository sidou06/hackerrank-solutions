#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Initialize the movement ranges for each direction
    r = n - c_q 
    l = c_q - 1
    u = n - r_q 
    d = r_q - 1
    ru = min(r,u)
    rd = min(r,d) 
    lu = min(l,u) 
    ld = min(l,d) 
    
    # Check if obstacles affect the queen's movement
    for ob in obstacles:
        ro = ob[0]
        co = ob[1] 
        if ro == r_q:
            if co > c_q:
                u = min(u, co - c_q - 1)
            else:
                d = min(d, c_q - co - 1)
        elif co == c_q:
            if ro > r_q:
                r = min(r, ro - r_q - 1)
            else:
                l = min(l, r_q - ro - 1)
        elif ro - r_q == co - c_q:
            if ro > r_q:
                ru = min(ru, ro - r_q - 1) 
            else:
                ld = min(ld, r_q - ro - 1)
        elif ro - r_q == c_q - co:
            if ro > r_q:
                lu = min(lu, ro - r_q - 1)
            else:
                rd = min(rd, r_q - ro - 1)

    # Return the total number of possible attacks the queen can make
    return u + d + l + r + ru + rd + lu + ld 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])

    # Read the obstacles positions
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    # Get the result and write to output
    result = queensAttack(n, k, r_q, c_q, obstacles)
    fptr.write(str(result) + '\n')

    fptr.close()