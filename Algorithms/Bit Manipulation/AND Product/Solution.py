#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'andProduct' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER a
#  2. LONG_INTEGER b
#

def andProduct(a, b):
    # Calculate the difference between the numbers
    diff = b - a
    tot = 0
    power = 1
    # Find the highest power of 2 less than or equal to the difference
    while diff >= power:
        power *= 2
    # Divide both a and b by the power and check if they are the same
    c = a // power 
    d = b // power 
    # If both are equal, return the result of c multiplied by power
    if c == d:
        return c * power
    else:
        # Otherwise, recursively call andProduct with the smaller range
        return power * andProduct(c, d)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read the number of test cases

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()  # Read the two integers for the range

        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])

        result = andProduct(a, b)  # Compute the result

        fptr.write(str(result) + '\n')  # Write the result to the output

    fptr.close()