#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'gridlandMetro' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track

def gridlandMetro(n, m, k, track):
    # Initialize count to keep track of covered cells
    count = 0
    # Dictionary to store tracks by row
    trains = {}
    for i in range(k):
        t = track[i]
        # Group tracks by their row
        if t[0] in trains:
            trains[t[0]].append([t[1], t[2]])
        else:
            trains[t[0]] = [[t[1], t[2]]]
    # Sort tracks in each row by start and end positions
    for t in trains:
        trains[t].sort(key = lambda x:(x[0],x[1]))
    # Calculate the total covered cells
    for t in trains:
        now_c1, now_c2 = -1, -1
        ligne = trains[t]
        for c in ligne:
            c1 = c[0]
            c2 = c[1]
            # Case where the current track does not overlap with the previous one
            if c1 > now_c2:
                count += c2 - c1 + 1
                now_c2 = c2
                now_c1 = c1
            # Case where the current track starts where the previous one ended
            elif c1 == now_c1:
                count += c2 - now_c2
                now_c2 = c2
            # Case where the current track extends beyond the previous one
            elif c2 > now_c2:
                count += c2 - now_c2
                now_c2 = c2
                now_c1 = c1
    # Return the total uncovered cells
    return n * m - count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()