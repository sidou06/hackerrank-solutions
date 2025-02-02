#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    tot = 0
    c.sort()  # Sort the costs in ascending order
    q = len(c) // k  # Calculate the number of complete sets
    b = len(c) % k  # Calculate the number of remaining items
    tot += sum(c[:b]) * (q + 1)  # Add the cost of the remaining items, multiplying by (q + 1) as they are bought more times
    while q > 0:
        tot += q * sum(c[b:b+k])  # Add the cost of a complete set of toys
        q -= 1  # Decrease the number of complete sets
        b += k  # Move the pointer for the next batch
    return tot

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input values
    nk = input().split()

    n = int(nk[0])  # Number of toys
    k = int(nk[1])  # Number of friends

    c = list(map(int, input().rstrip().split()))  # Costs of the toys

    # Calculate the minimum cost
    minimumCost = getMinimumCost(k, c)

    # Write the result to output
    fptr.write(str(minimumCost) + '\n')

    fptr.close()