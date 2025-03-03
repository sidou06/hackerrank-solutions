#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER m
#

def solve(a, m):
    # Check if m is 2 or a is 0, in which case return "YES"
    if m == 2 or a == 0:
        return "YES" 
    
    # Compute (m-1)/2
    p = (m - 1) // 2 
    
    # Compute a^p mod m using modular exponentiation
    r = pow(a, p, m) 
    
    # If the result is 1, return "YES", otherwise return "NO"
    if r == 1:
        return "YES"
    else:
        return "NO" 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])  # Read integer a
        m = int(first_multiple_input[1])  # Read integer m

        result = solve(a, m)  # Determine if condition is met

        fptr.write(result + '\n')

    fptr.close()