#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'movingTiles' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER s1
#  3. INTEGER s2
#  4. INTEGER_ARRAY queries
#

def movingTiles(l, s1, s2, queries):
    # Compute the time required for each query using the formula derived from relative speed
    return [((l - math.sqrt(query)) * math.sqrt(2)) / abs(s2 - s1) for query in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the first line of input and extract the values
    first_multiple_input = input().rstrip().split()

    l = int(first_multiple_input[0])  # Side length of the square
    s1 = int(first_multiple_input[1]) # Speed of first tile
    s2 = int(first_multiple_input[2]) # Speed of second tile

    # Read the number of queries
    queries_count = int(input().strip())

    queries = []

    # Read each query and store it in the list
    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    # Compute results for all queries
    result = movingTiles(l, s1, s2, queries)

    # Write the output results to file
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()