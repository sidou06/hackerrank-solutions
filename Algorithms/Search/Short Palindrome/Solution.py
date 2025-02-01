#!/bin/python3

import math
import os
import random
import re
import sys

def shortPalindrome(s):
    # Initialize an array to keep track of individual characters
    arr1 = [0]*26
    
    # Initialize a 2D array to keep track of pairs of characters
    arr2 = [[0]*26 for i in range(26)]
    
    # Initialize an array to keep track of triplets of characters
    arr3 = [0]*26
    
    # Initialize answer variable to store result
    ans = 0
    
    # Loop through the string characters
    for i in range(len(s)):
        # Calculate the index of the current character
        idx = ord(s[i]) - ord('a')
        
        # Add the count of valid triplets that can be formed with the current character
        ans += arr3[idx]
        
        # Update the triplet count for the current character
        for j in range(26):
            arr3[j] += arr2[j][idx]
        
        # Update the pair count for the current character
        for j in range(26):
            arr2[j][idx] += arr1[j]
        
        # Update the count for the current character
        arr1[idx] += 1
    
    # Return the result modulo 10^9 + 7
    return ans % (10**9+7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input string
    s = input()

    # Calculate the result by calling the function
    result = shortPalindrome(s)

    # Write the result to the output
    fptr.write(str(result) + '\n')

    fptr.close()