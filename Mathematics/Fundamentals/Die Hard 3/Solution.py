#!/bin/python3

import math
import os
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#

def solve(a, b, c):
    if c > max(a, b):  # Check if c is greater than the max of a and b
        return "NO"
    
    for i in range(1, max(a, b)):  # Iterate from 1 to the max of a and b
        if math.gcd(a, b) == math.gcd(i, c):  # Check if GCD condition holds
            return "YES"
    
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])  # Read a
        b = int(first_multiple_input[1])  # Read b
        c = int(first_multiple_input[2])  # Read c

        result = solve(a, b, c)  # Compute result

        fptr.write(result + '\n')  # Write output

    fptr.close()