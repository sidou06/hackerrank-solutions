#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Initialize counter for the valid pairs
    nb = 0
    
    # Iterate through all pairs
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Check if the sum of the pair is divisible by k
            if (ar[i] + ar[j]) % k == 0:
                nb += 1
    
    return nb

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the first line inputs n and k
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    # Read the array ar
    ar = list(map(int, input().rstrip().split()))

    # Call the function and get the result
    result = divisibleSumPairs(n, k, ar)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    fptr.close()