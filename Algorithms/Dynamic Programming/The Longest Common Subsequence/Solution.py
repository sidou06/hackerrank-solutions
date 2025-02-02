#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestCommonSubsequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def longestCommonSubsequence(a, b):
    # Get the lengths of the two input arrays
    m = len(a)
    n = len(b)
    # Initialize the DP table with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)] 
    
    # Fill the DP table
    for i in range(1,m + 1):
        for j in range(1,n + 1):
            # If the current elements match, increment the count from the diagonal
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            # Otherwise, take the max from the left or top
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    
    # Backtrack to get the LCS
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        # If the elements match, add to the LCS
        if a[i - 1] == b[j - 1]:
            lcs.append(a[i - 1])
            i -= 1
            j -= 1
        # Otherwise, move to the larger of the two neighboring cells
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    # Reverse the LCS since we backtracked
    return(reversed(lcs))  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the lengths of the two input arrays
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    # Read the arrays
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    # Get the longest common subsequence
    result = longestCommonSubsequence(a, b)

    # Write the result to the output
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()