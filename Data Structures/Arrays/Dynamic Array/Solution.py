#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Initialize result list to store answers to type 2 queries
    res = [] 
    # Variable to keep track of the last answer
    last = 0 
    # Create a list of empty lists, each representing a sequence
    arr = [] 
    for i in range(n):
        arr.append([]) 

    # Iterate through each query
    for query in queries:
        if query[0] == 1:
            # Calculate the index of the sequence to update
            arr[(query[1] ^ last) % n].append(query[2])
        else:
            # Retrieve value from sequence and update last answer
            last = arr[(query[1] ^ last) % n][query[2] % len(arr[(query[1] ^ last) % n])]
            res.append(last) 
    return res 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])  # Number of sequences
    q = int(first_multiple_input[1])  # Number of queries

    queries = []

    # Read all queries
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    # Compute the result of queries
    result = dynamicArray(n, queries)

    # Write the output to the file
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()