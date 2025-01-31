#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def is_pal(s):
    p = True
    i = 0
    while i < len(s) // 2 and p:
        if s[i] != s[len(s) - i - 1]:
            p = False 
        i += 1
    return p
    
def palindromeIndex(s):
    # Write your code here
    res = -1
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            j = len(s) - i - 1 
            if is_pal(s[:i] + s[i + 1:]):  # Check if removing character at i results in a palindrome
                return i 
            elif is_pal(s[:j] + s[j + 1:]):  # Check if removing character at j results in a palindrome
                return j 
            else:
                return -1  # If neither works, return -1
    return -1  # Return -1 if the string is already a palindrome

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())  # Read the number of test cases

    for q_itr in range(q):
        s = input()  # Read the string for each test case

        result = palindromeIndex(s)  # Call the function to find the index

        fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file