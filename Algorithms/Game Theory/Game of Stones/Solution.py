#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfStones' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def gameOfStones(n):
    # If the remainder when n is divided by 7 is 0 or 1, the second player wins
    if n % 7 <= 1:
        return "Second"
    # Otherwise, the first player wins
    else:
        return "First" 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        # Read the number of stones
        n = int(input().strip())

        # Determine the winner
        result = gameOfStones(n)

        # Write the result to output
        fptr.write(result + '\n')

    fptr.close()