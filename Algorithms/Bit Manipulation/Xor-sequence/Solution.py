#!/bin/python3

import math
import os
import random
import re
import sys

def my_xor(l):
    # Compute XOR from 0 to l based on pattern:
    # If l % 4 == 0, result is l
    # If l % 4 == 1, result is 1
    # If l % 4 == 2, result is l + 1
    # If l % 4 == 3, result is 0
    if l % 4 == 0:
        first = l
    elif l % 4 == 1:
        first = 1
    elif l % 4 == 2:
        first = l + 1
    else:
        first = 0
    return first

# Complete the xorSequence function below.
def xorSequence(l, r):
    sol = 0  # Initialize the result
    # Count how many full groups of 4 exist in the range
    fours = (r + 1) // 4 - ((l - 1) // 4) - 1
    if max(fours, 0) % 2:  # If the number of full groups is odd, XOR with 2
        sol = 2
    # Process remaining numbers that don't form full groups
    while l % 4 != 0 and l <= r:
        sol = sol ^ my_xor(l)
        l += 1
    if l <= r:
        while r % 4 != 3:
            sol = sol ^ my_xor(r)
            r -= 1
    return sol

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())  # Read the number of queries

    for q_itr in range(q):
        lr = input().split()  # Read l and r

        l = int(lr[0])
        r = int(lr[1])

        result = xorSequence(l, r)  # Compute the XOR sequence result

        fptr.write(str(result) + '\n')  # Write result to output

    fptr.close()