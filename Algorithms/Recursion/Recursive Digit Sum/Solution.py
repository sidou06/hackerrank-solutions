#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def sum_digits(x):
    # Compute the sum of digits in the string representation of a number
    s = 0
    for c in x:
        s += int(c)
    return str(s)

def superDigit(n, k):
    # Base case: if k is 1 and n is a single digit, return it as an integer
    if k == 1 and len(n) == 1:
        return int(n) 
    
    # If k is 1, recursively compute the super digit of the sum of digits of n
    elif k == 1:
        return superDigit(sum_digits(n), k)
    
    # If n is a single digit, multiply it by k and compute its super digit
    elif len(n) == 1:
        return superDigit(str(int(n) * k), 1)
    
    # Otherwise, recursively compute the super digit of the sum of digits of n
    else:
        return superDigit(sum_digits(n), k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])

    # Compute the result
    result = superDigit(n, k)

    # Write output result to file
    fptr.write(str(result) + '\n')
    fptr.close()