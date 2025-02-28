#!/bin/python3

import math
import os
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. 2D_INTEGER_ARRAY queries
#

def solve(arr, queries):
    res = []  # List to store results
    for x1, x2 in queries:  # Iterate over queries
        if x2 < x1:  # If the second index is smaller than the first
            res.append("Odd")
        else:
            if arr[x1 - 1] % 2 == 1 or (arr[x1 - 1] % 2 == 0 and x2 > x1 and arr[x1] == 0):
                res.append("Odd")
            else: 
                res.append("Even")
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())  # Read the number of elements in arr

    arr = list(map(int, input().rstrip().split()))  # Read arr elements

    q = int(input().strip())  # Read the number of queries

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))  # Read queries

    result = solve(arr, queries)

    fptr.write('\n'.join(result))  # Write results to output
    fptr.write('\n')

    fptr.close()