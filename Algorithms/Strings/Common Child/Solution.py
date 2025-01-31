#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Initialize a 2D array to store the length of the longest common subsequence
    lcs = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
    
    # Iterate through each character of both strings
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            # If characters match, increase the count for the LCS at this point
            if s1[i - 1] == s2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                # If characters don't match, take the max value from either top or left cell
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    
    # Return the length of the longest common subsequence
    return lcs[-1][-1] 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()  # Input string s1
    s2 = input()  # Input string s2

    result = commonChild(s1, s2)  # Call the function to find the common child

    fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()