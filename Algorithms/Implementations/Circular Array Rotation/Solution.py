#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Since the array is rotated k times, to avoid repetitive rotations,
    # we can use the modulo operator to simplify the rotation.
    # For example, if k is greater than the length of the array, rotating more than once
    # will result in the same configuration after `k % len(a)` rotations.
    
    k = k % len(a)  # Minimize unnecessary rotations
    
    res = []
    for i in range(len(queries)):
        # For each query, subtract k to get the new index of the rotated array
        queries[i] -= k
        queries[i] %= len(a)  # Ensure the index stays within the bounds of the array
        res.append(a[queries[i]])  # Append the element at the new index to the result

    return res  # Return the final result after all queries are processed.

if __name__ == '__main__':
    # Open the output file to write the result.
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values.
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])  # Length of the array
    k = int(first_multiple_input[1])  # Number of rotations
    q = int(first_multiple_input[2])  # Number of queries

    # Read the array elements.
    a = list(map(int, input().rstrip().split()))

    # Read all the queries.
    queries = []
    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    # Call the circularArrayRotation function and get the result.
    result = circularArrayRotation(a, k, queries)

    # Write the result to the output file.
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    # Close the output file after writing the results.
    fptr.close()