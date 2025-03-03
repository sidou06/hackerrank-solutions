#!/bin/python3

import math
import os
import random
import re
import sys

from math import gcd as g 

if __name__ == '__main__':
    n = int(input().strip())  # Read input size

    a = list(map(int, input().rstrip().split()))  # Read input list

    # Handle single-element case
    if n == 1:
        print(a[0] + 1)
    else:
        pre = [0] * len(a)  # Prefix GCD array
        suf = [0] * len(a)  # Suffix GCD array

        # Compute prefix GCD
        for i in range(len(a)):
            if i == 0:
                pre[i] = a[i]
            else:
                pre[i] = g(pre[i - 1], a[i])

        # Compute suffix GCD
        for i in range(len(a) - 1, -1, -1):
            if i == len(a) - 1:
                suf[i] = a[i]
            else:
                suf[i] = g(suf[i + 1], a[i])

        # Compute final GCD array excluding one element at a time
        final_prefix = []
        for i in range(len(a)):
            if i == 0:
                final_prefix.append(suf[i + 1])  # Excluding first element
            elif i == len(a) - 1:
                final_prefix.append(pre[i - 1])  # Excluding last element
            else:
                final_prefix.append(g(pre[i - 1], suf[i + 1]))  # Excluding middle elements

        # Find the first unique GCD value
        net = {}
        for i in final_prefix:
            if i in net:
                net[i] += 1
            else:
                net[i] = 1

        for i in net:
            if net[i] == 1:
                ans = i
                break
        
        print(ans)  # Output the result