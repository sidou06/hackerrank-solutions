#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nimbleGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def nimbleGame(s):
    # Initialize cumulative XOR result
    cp = 0 

    # Iterate through the list and XOR the index if the value at that index is odd
    for i in range(len(s)):
        if s[i] % 2 == 1:
            cp ^= i 
    
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
        # Read the size of the array
        n = int(input().strip())

        # Read the array elements
        s = list(map(int, input().rstrip().split()))

        # Compute the result
        result = nimbleGame(s)

        # Write result to output
        fptr.write(result + '\n')

    fptr.close()