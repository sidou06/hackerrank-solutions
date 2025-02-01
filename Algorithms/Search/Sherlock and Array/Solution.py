#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'balancedSums' function below.
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.

def balancedSums(arr):
    # Calculate the total sum of the array
    s = sum(arr) 
    i = 0
    tmp = 0
    # Traverse the array and check if there's an index where the sum of elements
    # on the left is equal to the sum of elements on the right
    while i < len(arr):
        if tmp == (s - arr[i]) / 2:
            return "YES" 
        tmp += arr[i] 
        i += 1
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()