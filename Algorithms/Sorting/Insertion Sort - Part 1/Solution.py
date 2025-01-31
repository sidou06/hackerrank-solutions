#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Store the last element to be inserted
    v = arr[-1]
    i = n - 2  # Start from the second last element

    # Shift elements to the right until the correct position for v is found
    while i >= 0 and arr[i] > v:
        arr[i + 1] = arr[i]
        print(" ".join(map(str, arr)))
        i -= 1

    # Insert the element at the correct position
    arr[i + 1] = v
    print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)