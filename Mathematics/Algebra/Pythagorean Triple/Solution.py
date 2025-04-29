#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pythagoreanTriple' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER a as parameter.
#

def pythagoreanTriple(a):
    # Initialize the list to hold the Pythagorean triple
    # For even a, we use the formula: a, (a/2)^2 - 1, (a/2)^2 + 1
    if a % 2 == 0:
        k = a // 2
        res = [a, k ** 2 - 1, k ** 2 + 1]
    # For odd a, we use the formula: a, 2k(k+1), k^2 + (k+1)^2 where a = 2k + 1
    else:
        k = (a - 1) // 2
        res = [a, 2 * k * (k + 1), (k + 1) ** 2 + k ** 2]
    return res  # Return the Pythagorean triple

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file

    a = int(input().strip())  # Read input value

    triple = pythagoreanTriple(a)  # Compute the triple

    fptr.write(' '.join(map(str, triple)))  # Write triple to file
    fptr.write('\n')

    fptr.close()  # Close file