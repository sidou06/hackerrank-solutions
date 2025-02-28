#!/bin/python3

import math
import os
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def solve(n, m):
    num = math.factorial(n + m - 1)  # Compute factorial of (n + m - 1)
    den = math.factorial(n) * math.factorial(m - 1)  # Compute denominator as factorial(n) * factorial(m-1)
    return (num // den) % (10**9 + 7)  # Compute result modulo 10^9 + 7

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])  # Read n
        m = int(first_multiple_input[1])  # Read m

        result = solve(n, m)

        fptr.write(str(result) + '\n')  # Write output

    fptr.close()