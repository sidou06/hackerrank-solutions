#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

# Define the alphabet string for reference
alpha = "abcdefghijklmnopqrstuvwxyz"

def weightedUniformStrings(s, queries):
    # Initialize a set to store uniform substring weights
    w = [] 
    # Track the current character
    c = s[0]
    # Initialize coefficient for consecutive occurrences
    coeff = 1

    # Iterate through the string to calculate uniform substring weights
    for i in range(len(s)):
        pos = alpha.index(s[i]) + 1  # Get character weight

        if s[i] == c:
            # If the character is repeated, multiply by its occurrence count
            w.append(pos * coeff)
            coeff += 1
        else:
            # Reset for a new character
            w.append(pos)
            coeff = 2 
            c = s[i] 

    # Convert list to a set for faster lookups
    w = set(w) 

    # Check if each query is in the computed weights
    return ["Yes" if ele in w else "No" for ele in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()  # Read input string

    queries_count = int(input().strip())  # Read number of queries

    queries = []  # Initialize query list

    # Read query values
    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)  # Compute results

    fptr.write('\n'.join(result))  # Write output to file
    fptr.write('\n')

    fptr.close()  # Close the output file