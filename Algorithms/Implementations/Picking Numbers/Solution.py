#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Initialize minimum and maximum values
    mini = min(a)
    maxi = max(a)
    
    # If all elements are the same, return the length of the array
    if maxi == mini:
        return len(a)
    
    # Create a list to count the occurrences of numbers
    count = []
    for j in range(maxi - mini + 1):
        count.append(0)
    
    # Count the occurrences of each number in the list
    for i in range(len(a)):
        count[a[i] - mini] += 1
    
    # Find the maximum sum of adjacent counts
    tot = 0
    for k in range(maxi - mini):
        if count[k] + count[k + 1] > tot:
            tot = count[k] + count[k + 1]
    
    return tot

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()