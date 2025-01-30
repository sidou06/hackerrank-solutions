#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # If the sum of lengths of both strings is less than or equal to k, return 'Yes'
    if len(s) + len(t) <= k:
        return 'Yes'
    else:
        i = 0
        # Find the common prefix length between the two strings
        while i < min(len(s), len(t)) and s[i] == t[i]:
            i += 1
        # Calculate the number of operations required
        a = s[i:]  # Remaining part of s after the common prefix
        b = t[i:]  # Remaining part of t after the common prefix
        d = len(a) + len(b)
        
        # Check if the number of operations is less than or equal to k and if (k - d) is even
        if d <= k and (k - d) % 2 == 0:
            return 'Yes'
        else:
            return 'No'
            
if __name__ == '__main__':
    # Read input for the two strings and the value of k
    s = input()
    t = input()
    k = int(input().strip())

    # Call the appendAndDelete function and print the result
    result = appendAndDelete(s, t, k)

    # Write the result to the output file
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(result + '\n')
    fptr.close()