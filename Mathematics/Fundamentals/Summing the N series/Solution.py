#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'summingSeries' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def summingSeries(n):
    # Compute the sum of the series using the formula n^2 mod (10^9 + 7)
    return (n ** 2) % (10**9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        # Read the input value n for each test case
        n = int(input().strip())

        # Compute and write the result
        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()