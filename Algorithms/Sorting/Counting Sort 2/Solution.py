#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Initialize a list of size 100 with zeros
    res = [0] * 100
    
    # Count occurrences of each number in arr
    for i in arr:
        res[i] += 1
    
    sorted_arr = []
    for i in range(100):
        sorted_arr.extend([i] * res[i])
    
    return sorted_arr 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()