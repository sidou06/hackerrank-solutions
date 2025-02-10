#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):
    # If all piles contain only one stone
    if max(s) == 1:
        # If the number of piles is even, the first player wins
        if len(s) % 2 == 0:
            return "First"
        # Otherwise, the second player wins
        return "Second" 
    
    # Initialize cumulative XOR result
    cp = 0 
    # Compute XOR of all pile sizes
    for ele in s:
        cp = cp ^ ele 
    
    # If the XOR result is zero, the second player wins
    if cp == 0:
        return "Second"
    
    # Otherwise, the first player wins
    return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        # Read number of piles
        n = int(input().strip())

        # Read pile sizes
        s = list(map(int, input().rstrip().split()))

        # Compute the result
        result = misereNim(s)

        # Write result to output
        fptr.write(result + '\n')

    fptr.close()