#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(B):
    # Write your code here
    n = len(B)
    hi = 0
    low = 0
    for i in range(1, n):
        high_to_low = abs(B[i - 1] - 1)
        low_to_high = abs(B[i] - 1)
        high_to_high = abs(B[i] - B[i - 1])
        
        new_hi = max(low + low_to_high, hi + high_to_high)
        new_low = max(low, hi + high_to_low)
        
        hi = new_hi
        low = new_low
    return max(hi, low)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()