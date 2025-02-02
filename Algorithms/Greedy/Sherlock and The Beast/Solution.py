#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    # Initialize result string
    res = ''
    
    # Find the maximum number of 5s that can be used (must be a multiple of 3)
    five = (n // 3) * 3
    
    # Iterate while ensuring the remaining count is a multiple of 5
    while five >= 0 and res == '':
        three = n - five  # Remaining count for 3s
        if three % 5 == 0:  # If valid, construct the number
            res = '5' * five + '3' * three
        five -= 3  # Reduce 5s by multiples of 3 to check for a valid combination
    
    # Print result, if no valid number is found, print -1
    print(res if res else -1)

if __name__ == '__main__':
    # Read number of test cases
    t = int(input().strip())

    # Process each test case
    for t_itr in range(t):
        n = int(input().strip())
        decentNumber(n)