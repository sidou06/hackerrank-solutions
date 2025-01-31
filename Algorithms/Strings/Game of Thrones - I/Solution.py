#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here
    counts = []  # Initialize a list to store counts of each character
    odd = 0  # Initialize a counter for odd occurrences
    alpha = "abcdefghijklmnopqrstuvwxyz"  # The alphabet to check
    for c in alpha:  # Iterate through each character in the alphabet
        if c in s:  # If the character is present in the string
            counts.append(s.count(c))  # Append the count of that character
    for i in counts:  # Iterate through the character counts
        if i % 2 != 0:  # If the count is odd
            odd += 1  # Increment the odd counter
    if odd > 1:  # If there is more than one odd count
        return "NO"  # Return "NO" as the string can't form a palindrome
    else:
        return "YES"  # Return "YES" if the string can form a palindrome

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file

    s = input()  # Read the input string

    result = gameOfThrones(s)  # Call the function to get the result

    fptr.write(result + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file