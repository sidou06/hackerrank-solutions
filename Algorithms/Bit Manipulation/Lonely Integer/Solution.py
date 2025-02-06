#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    i = 0
    # Loop through the list to find the unique element
    while a.count(a[i]) != 1:
        i += 1
    return a[i] 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input value n (not actually needed in logic)
    n = int(input().strip())

    # Read the list of integers
    a = list(map(int, input().rstrip().split()))

    # Get the unique integer
    result = lonelyinteger(a)

    # Write the result to output
    fptr.write(str(result) + '\n')

    fptr.close()