#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Sort the array to group matching socks together
    ar.sort() 
    i = pairs = 0
    # Iterate through the list of socks
    while i < n - 1:
        # If the current sock matches the next one
        if ar[i] == ar[i + 1]:
            pairs += 1  # Increment the pair counter
            i += 2  # Move to the next pair of socks
        else:
            i += 1  # Move to the next sock
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Number of socks

    ar = list(map(int, input().rstrip().split()))  # List of socks

    result = sockMerchant(n, ar)  # Calculate the number of matching pairs

    fptr.write(str(result) + '\n')

    fptr.close()