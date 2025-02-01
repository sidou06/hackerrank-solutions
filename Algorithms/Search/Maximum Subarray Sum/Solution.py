#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'maximumSum' function below.
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m

from bisect import bisect_right

def maximumSum(a, m):
    l = []
    su = 0
    r = 0
    # Iterate through the array and calculate the cumulative sum mod m
    for i in range(len(a)):
        su += a[i]
        su %= m
        # Find the position where the sum can be inserted to keep the list sorted
        it = bisect_right(l, su) 
        if it != len(l):
            # Update the result if a better one is found
            r = max(r, su - l[it] + m)
            l.insert(it, su)
        else:
            r = max(r, su)
            l.append(su)
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()