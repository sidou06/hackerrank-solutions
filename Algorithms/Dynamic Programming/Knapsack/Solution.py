#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unboundedKnapsack(k, arr):
    # Initialize the dp array with zeros. dp[i] represents the number of ways to form the weight i.
    t = 0
    dp = [0] * (k + 1)
    # There is 1 way to form weight 0 (by taking nothing).
    dp[0] += 1
    # Sort the array to iterate in ascending order of item weights
    arr.sort()
    # Loop through each element in the array
    for elem in arr:
        # Update the dp array for all values from elem to k
        for i in range(elem,k + 1):
            dp[i] += dp[i - elem]
    # Find the largest weight less than or equal to k that can be formed
    sol = k
    while dp[sol] == 0:
        sol -= 1
    return sol

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Input number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input n (number of items) and k (maximum weight)
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        # Input item weights and remove duplicates
        arr = list(set(map(int, input().rstrip().split())))
    
        # Get the result for the current test case
        result = unboundedKnapsack(k, arr)

        # Write the result to the output
        fptr.write(str(result) + '\n')

    fptr.close()