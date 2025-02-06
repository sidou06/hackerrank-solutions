#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Initialize the number of bribes
    bribes = 0
    i = 0

    while i < len(q):
        # Check if a person has moved more than 2 positions forward
        if q[i] > i + 3:
            print("Too chaotic")
            return None
        
        # Count the number of bribes received by the current person
        for j in range(max(q[i] - 2, 0), i):
            if q[i] < q[j]:
                bribes += 1
        
        i += 1

    # Print the total number of bribes
    print(bribes)
    return None 

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)