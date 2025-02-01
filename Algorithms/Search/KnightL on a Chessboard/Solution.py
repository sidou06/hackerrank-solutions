#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'knightlOnAChessboard' function below.
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.

def knightlOnAChessboard(n):
    res = [[]]
    # Iterate over all possible knight moves
    for a in range(1, n):
        for b in range(1, n):
            old = [[0, 0]]
            new = [[0, 0]]
            cpt = 0
            # Process the knight's movement until the target is reached
            while True:
                future = [] 
                for pos in new:
                    i = pos[0] 
                    j = pos[1] 
                    # Check all 8 possible moves for the knight
                    if i - a >= 0 and j - b >= 0 and [i - a, j - b] not in old:
                        future.append([i - a, j - b])
                        old.append([i - a, j - b])
                    if i - a >= 0 and j + b < n and [i - a, j + b] not in old:
                        future.append([i - a, j + b])
                        old.append([i - a, j + b])
                    if i + a < n and j - b >= 0 and [i + a, j - b] not in old:
                        future.append([i + a, j - b])
                        old.append([i + a, j - b])
                    if i + a < n and j + b < n and [i + a, j + b] not in old:
                        future.append([i + a, j + b])
                        old.append([i + a, j + b])
                    if i - b >= 0 and j - a >= 0 and [i - b, j - a] not in old:
                        future.append([i - b, j - a])
                        old.append([i - b, j - a])
                    if i - b >= 0 and j + a < n and [i - b, j + a] not in old:
                        future.append([i - b, j + a]) 
                        old.append([i - b, j + a])
                    if i + b < n and j - a >= 0 and [i + b, j - a] not in old:
                        future.append([i + b, j - a])
                        old.append([i + b, j - a])
                    if i + b < n and j + a < n and [i + b, j + a] not in old:
                        future.append([i + b, j + a])
                        old.append([i + b, j + a])
                cpt += 1
                # Break if there are no more possible moves
                if future == []:
                    res[a - 1].append(-1)
                    break 
                # Check if the target (n-1, n-1) has been reached
                if [n - 1, n - 1] in future:
                    res[a - 1].append(cpt)
                    break 
                new = future 
        res.append([])

    # Return the result excluding the last empty list
    return res[: -1]   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()