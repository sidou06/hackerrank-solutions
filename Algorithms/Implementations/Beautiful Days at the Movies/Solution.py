#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#
def inverse(x):
    ch = str(x)
    res = 0
    for i in range(len(ch)):
        res = res + int(ch[i]) * pow(10,i)
    return res

def beautifulDays(i, j, k):
    # Write your code here
    tot = 0
    for x in range(i, j + 1):
        y = inverse(x)
        if abs(y - x) % k == 0:
            tot += 1
    return tot

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()