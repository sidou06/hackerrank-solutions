#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    subsequence = 0
    subarray = 0
    m = max(arr)
    cur = 0
    sol = m
    if m <= 0:
        return [m,m]
    for i in range(len(arr)):
        cur += arr[i]
        if arr[i] > 0:
            subsequence += arr[i]
            sol = max(sol,cur)
        else:
            if cur < 0:
                cur = 0
    return [sol,subsequence]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()