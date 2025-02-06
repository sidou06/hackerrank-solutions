#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # If n is 0, there's only one valid way (choosing 0)
    if n == 0:
        return 1
    
    cp = 0  # Count of zero bits in n
    while n > 1:
        if n % 2 == 0:  # Check if the current bit is 0
            cp += 1
        n //= 2  # Shift n to the right (divide by 2)
    
    return 2 ** cp  # The result is 2 raised to the count of zero bits

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read input integer

    result = sumXor(n)  # Compute sumXor result

    fptr.write(str(result) + '\n')  # Write result to output

    fptr.close()