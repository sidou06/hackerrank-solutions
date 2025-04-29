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
# The function accepts LONG_INTEGER s as parameter.
#

def solve(s):
    # Calculate the number of times 20 fits in s
    a = s // 20
    # Adjust the value of a if s is perfectly divisible by 20
    if s % 20 == 0:
        a -= 1 
    # Return the result after applying the formula and modulo operation
    return ((s + a) * 2) % (10 ** 9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    t = int(input().strip())

    # Iterate over each test case
    for t_itr in range(t):
        # Read the input value for s
        s = int(input().strip())

        # Calculate the result using the solve function
        result = solve(s)

        # Write the result to the output
        fptr.write(str(result) + '\n')

    fptr.close()
