#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def solve(a, b):
    m = 10 ** 9 + 7  # Modulo value
    base = 0 
    power = 0 

    # Convert string 'a' to an integer modulo m
    for digit in a:
        base = (base * 10 + int(digit)) % m 

    # Convert string 'b' to an integer modulo (m - 1)
    for digit in b:
        power = (power * 10 + int(digit)) % (m - 1)

    # Compute (base^power) % m
    return pow(base, power, m) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        a = first_multiple_input[0]  # Read first number as string
        b = first_multiple_input[1]  # Read second number as string

        result = solve(a, b)

        fptr.write(str(result) + '\n')  # Write output

    fptr.close()