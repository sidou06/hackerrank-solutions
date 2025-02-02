#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right
#
# Complete the 'sherlockAndMinimax' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER p
#  3. INTEGER q
#

def sherlockAndMinimax(arr, p, q):
    # Write your code here
    arr.sort()
    n = len(arr)
    left = bisect_right(arr,p)
    right = bisect_right(arr,q)
    sol = 0
    m = 0
    if left == n:
        return q
    if right == 0:
        return p
    if left == 0:
        if arr[0] - p > m:
            m = arr[0] - p
            sol = p
    else:
        moy = (arr[left] + arr[left - 1]) // 2
        if moy in range(p,q + 1) and moy - arr[left - 1] > m:
            m = moy - arr[left - 1]
            sol = moy
        if p <= moy and p - arr[left - 1] > m:
            m = p - arr[left - 1]
            sol = p
        elif p > moy and arr[left] - p > m:
            m = arr[left] - p
            sol = p
            
    for k in range(left, right - 1):
        if (arr[k] + arr[k + 1]) // 2 - arr[k] > m:
            m = (arr[k] + arr[k + 1]) // 2 - arr[k]
            sol = (arr[k] + arr[k + 1]) // 2
            
    if right == n:
        if q - arr[n - 1] > m:
            m = q - arr[n - 1]
            sol = q
    else:
        moy = (arr[right] + arr[right - 1]) // 2
        if moy in range(p,q + 1) and moy - arr[right - 1] > m:
            m = moy - arr[right - 1]
            sol = moy
        if q <= moy and q - arr[right - 1] > m:
            m = q - arr[right - 1]
            sol = q
        elif q > moy and arr[right] - q > m:
            m = arr[right] - q
            sol = q
    return sol
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    result = sherlockAndMinimax(arr, p, q)

    fptr.write(str(result) + '\n')

    fptr.close()