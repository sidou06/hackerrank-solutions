#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # Write your code here
    mod = 10 ** 9 + 7
    possible_line = [1]
    for i in range(1, m + 1):
        possible_line.append(sum(possible_line[-4:]) % mod)
    totals_with_invalid = []
    for i in range(m + 1):
        totals_with_invalid.append(pow(possible_line[i], n, mod))
    invalid = [0, 0]
    for i in range(2, m + 1):
        inv = 0
        for j in range(1, i):
            left = totals_with_invalid[j] - invalid[j]
            right = totals_with_invalid[i - j]
            inv = (inv + (left * right)) % mod
        invalid.append(inv)
    return (totals_with_invalid[-1] - invalid[-1]) % mod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()