#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Compute the factorial of n and print the result
    print(math.factorial(n))

if __name__ == '__main__':
    # Read the input value for n
    n = int(input().strip())

    # Call the extraLongFactorials function to print the result
    extraLongFactorials(n)