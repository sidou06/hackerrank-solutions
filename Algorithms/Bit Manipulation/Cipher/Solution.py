#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. STRING s
#

def cipher(k, s):
    # Initialize the result with the first character of the string
    result = s[0]
    
    # Apply XOR operation for the first part
    for i in range(1, min(len(s) - k + 1, k)):
        result += str(int(s[i - 1]) ^ int(s[i]))
    
    tmp = 0
    # Check if the length of s is larger than k to continue processing
    if k < len(s) - k + 1:
        for p in range(1, k):
            tmp ^= int(result[p])
        tmp ^= int(s[k])
        result += str(tmp)
    
    # Continue the XOR operation for the rest of the string
    for j in range(k + 1, len(s) - k + 1):
        tmp = int(s[j]) ^ int(s[j - 1]) ^ int(result[j - k])
        result += str(tmp)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    # Get the cipher result
    result = cipher(k, s)

    # Write the result to output
    fptr.write(result + '\n')

    fptr.close()