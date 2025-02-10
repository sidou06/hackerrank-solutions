#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nimGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY pile as parameter.
#

def nimGame(pile):
    # Initialize cumulative XOR result
    cp = 0
    # Compute XOR of all pile sizes
    for ele in pile:
        cp = cp ^ ele 
    # If result is non-zero, first player has a winning strategy
    if cp != 0:
        return "First"
    # Otherwise, second player wins
    return "Second"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of games
    g = int(input().strip())

    for g_itr in range(g):
        # Read number of piles
        n = int(input().strip())

        # Read pile sizes
        pile = list(map(int, input().rstrip().split()))

        # Compute the result
        result = nimGame(pile)

        # Write result to output
        fptr.write(result + '\n')

    fptr.close()