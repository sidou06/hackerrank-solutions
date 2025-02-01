#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'icecreamParlor' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr

def icecreamParlor(m, arr):
    # Iterate through the array to find two ice creams that sum up to m
    for i in range(len(arr)):
        # Check if the complementary flavor exists in the rest of the array
        if (m - arr[i]) in arr[i + 1:]:
            # Find the 1-based index of the first and second ice creams
            ind1 = i + 1
            ind2 = arr[i+1:].index(m - arr[i]) + i + 2
            return [ind1, ind2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()