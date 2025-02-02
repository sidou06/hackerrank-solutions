#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#

m = 10 ** 9 + 7

def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    uns = 0
    autres = 1
    for i in range(n - 3):
        uns = (autres * (k - 1)) % m
        if i % 2:
            autres = (uns + 1 ) % m
        else:
            autres = (uns - 1) % m
    if x == 1:
        return (autres * (k - 1)) % m
    return (autres * (k - 2) + uns) % m
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()