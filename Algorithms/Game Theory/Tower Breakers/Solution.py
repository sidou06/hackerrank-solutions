#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n (number of towers)
#  2. INTEGER m (height of each tower)
#

def towerBreakers(n, m):
    # If the height of all towers is 1, Player 1 has no valid moves, so Player 2 wins
    if m == 1 or n % 2 == 0:
        return 2
    # Otherwise, Player 1 wins by making the first move strategically
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        # Read n (number of towers) and m (height of each tower)
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])

        # Compute the winner
        result = towerBreakers(n, m)

        # Write result to output
        fptr.write(str(result) + '\n')

    fptr.close()