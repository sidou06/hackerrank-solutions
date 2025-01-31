#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # Write your code here
    common = "NO"  # Assume no common character by default
    if len(s1) < len(s2):  # Check the shorter string to optimize
        s = s1  # Assign the shorter string to s
        sp = s2  # Assign the longer string to sp
    else:
        s = s2  # Assign the shorter string to s
        sp = s1  # Assign the longer string to sp
    c = 0  # Initialize the index for iteration
    while c < len(s) and common == "NO":  # Iterate through the shorter string
        if s[c] in sp:  # Check if the character is in the longer string
            common = "YES"  # If found, set common to "YES"
        c += 1  # Move to the next character
    return common  # Return the result (YES or NO)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file

    q = int(input().strip())  # Read the number of test cases

    for q_itr in range(q):  # Iterate through each test case
        s1 = input()  # Read the first string
        s2 = input()  # Read the second string

        result = twoStrings(s1, s2)  # Call the function to check for common characters

        fptr.write(result + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file