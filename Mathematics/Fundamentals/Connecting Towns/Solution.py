#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectingTowns' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY routes
#

def connectingTowns(n, routes):
    # Initialize total number of ways with 1
    total = 1
    # Loop through each route and multiply the total number of ways
    for i in range(n - 1):
        total = (total * routes[i]) % 1234567  # Use modulo to prevent overflow
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        # Read number of towns
        n = int(input().strip())

        # Read the routes between towns
        routes = list(map(int, input().rstrip().split()))

        # Compute and write the result
        result = connectingTowns(n, routes)

        fptr.write(str(result) + '\n')

    fptr.close()