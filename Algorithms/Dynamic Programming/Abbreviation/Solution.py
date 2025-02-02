#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    # Write your code here
    n, m = len(a), len(b)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] and a[i - 1].islower()
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1].lower() == b[j - 1].lower():
                dp[i][j] = dp[i - 1][j - 1] or (a[i - 1].islower() and dp[i - 1][j])
            elif a[i - 1].islower():
                dp[i][j] = dp[i - 1][j]
    return "YES" if dp[n][m] else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()