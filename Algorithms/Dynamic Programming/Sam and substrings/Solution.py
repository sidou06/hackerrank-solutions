#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#
m = 10 ** 9 + 7
def substrings(n):
    # Write your code here
    som = 0
    prev = 0
    for i, nb in enumerate(n):
        prev = prev * 10 + int(nb) * (i + 1)
        prev %= m
        som += prev
        som %= m
    return som

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()