#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimal_swaps(arr,asc):
    org = arr.copy()
    dic = {}
    n = len(org)
    for i in range(n):
        dic[org[i]] = i
    swap = 0
    for i in range(n):
        if org[i] != asc[i]:
            swap += 1
            ind = dic[asc[i]]
            dic[org[i]] = ind 
            org[i], org[ind] = org[ind], org[i]
    return swap
            

def lilysHomework(arr):
    n = len(arr)
    # Write your code here
    try1 = sorted(arr)
    try2 = []
    for i in range(n):
        try2.append(try1[n - i - 1])
    return min(minimal_swaps(arr,try1), minimal_swaps(arr,try2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()