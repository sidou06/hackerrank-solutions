#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'missingNumbers' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr

def missingNumbers(arr, brr):
    # Initialize an empty list to store missing numbers
    res = []
    # Iterate through the elements of brr to find missing numbers in arr
    for di in brr:
        # If the element is not in arr, it's missing
        if di not in arr:
            res.append(di) 
        else:
            # Remove the matched element from arr
            arr.pop(arr.index(di))
    # Remove duplicates by converting the result to a set and sort it
    res = list(set(res))
    res.sort() 
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()