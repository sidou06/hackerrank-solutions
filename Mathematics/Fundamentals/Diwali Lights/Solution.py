#!/bin/python3

import math
import os
import sys

#
# Complete the 'lights' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER n as parameter.
#

def lights(n):
    return ((2**n) % 10**5) - 1  # Compute the result using modular exponentiation

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read the number of test cases

    for t_itr in range(t):
        n = int(input().strip())  # Read the input value

        result = lights(n)

        fptr.write(str(result) + '\n')  # Write the result to output

    fptr.close()