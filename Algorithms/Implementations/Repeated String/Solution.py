#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Initialize the count of 'a' in the string s
    nb = 0
    for i in range(len(s)):
        if s[i] == 'a':
            nb += 1
    
    # Calculate how many full repetitions of s fit into n
    t = (n // len(s)) * nb
    
    # Calculate the remaining part after full repetitions
    r = n % len(s)
    
    # Count the 'a's in the remaining part
    for i in range(r):
        if s[i] == 'a':
            t += 1
    
    return t

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the string s and the long integer n
    s = input()
    n = int(input().strip())

    # Call the repeatedString function
    result = repeatedString(s, n)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()