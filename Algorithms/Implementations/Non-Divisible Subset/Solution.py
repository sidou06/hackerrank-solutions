#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Initialize a dictionary to count occurrences of remainders when divided by k
    d = dict() 
    tot = 0
    
    # Initialize the dictionary with all possible remainders
    for i in range(k):
        d[i] = 0 
        
    # Count the occurrences of each remainder when elements in s are divided by k
    for ele in s:
        d[ele % k] += 1
    
    # Iterate through the possible remainders and calculate the size of the subset
    for i in range(k // 2 + 1):
        j = k - i 
        if i == 0:
            # If remainder is 0, include at most one element
            tot += min(1,d[i])
        elif i == k // 2 and k % 2 == 0:
            # If remainder is half of k (and k is even), include at most one element
            tot += min(1,d[i])
        else:
            # For other remainders, include the maximum count between the pair of remainders
            tot += max(d[i],d[j])
    
    return tot 
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input values
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))

    # Call the nonDivisibleSubset function
    result = nonDivisibleSubset(k, s)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()