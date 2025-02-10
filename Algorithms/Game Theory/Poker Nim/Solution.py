#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pokerNim' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY c
#

def pokerNim(k, c):
    # Initialize cumulative XOR result
    pc = 0

    # Iterate through the list and XOR each pile size
    for ele in c:
        pc ^= ele 

    # If the XOR result is zero, the second player wins
    if pc == 0:
        return "Second"

    # Otherwise, the first player wins
    return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        # Read n (number of piles) and k (maximum number of chips per move)
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])

        # Read the pile sizes
        c = list(map(int, input().rstrip().split()))

        # Compute the result
        result = pokerNim(k, c)

        # Write result to output
        fptr.write(result + '\n')

    fptr.close()