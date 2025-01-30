#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Ensure the page numbers are adjusted if necessary
    if n % 2 == 0:
        n = n + 1  # If n is even, adjust it to be odd
    if p % 2 == 0:
        p = p + 1  # If p is even, adjust it to be odd
    
    # Calculate the number of turns from the front and from the back
    a = (p - 1) // 2  # Number of turns from the front
    b = (n - p) // 2  # Number of turns from the back
    
    # Return the minimum of both options
    return min(a, b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Total number of pages

    p = int(input().strip())  # Page to turn to

    result = pageCount(n, p)  # Calculate the minimum number of pages to turn

    fptr.write(str(result) + '\n')

    fptr.close()