#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    # Write your code here
    mini = min(arr)
    sol = 10 ** 9
    for l in range(5):
        tra = 0
        m = mini - l
        for ele in arr:
            diff = ele - m
            tra += diff // 5 + (diff % 5) // 2 + (diff % 5) % 2
        sol = min(sol, tra)
    return sol

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()