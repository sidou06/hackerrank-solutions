#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    # Write your code here
    deleted = 0  # Initialize the count of deleted characters
    alphab = "abcdefghijklmnopqrstuvwxyz"  # Define the alphabet
    for ch in alphab:  # Iterate through each letter of the alphabet
        # Calculate the difference in the count of each character in both strings
        deleted += abs(s1.count(ch) - s2.count(ch)) 
    return deleted  # Return the total number of deletions required

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file

    s1 = input()  # Read the first string

    s2 = input()  # Read the second string

    result = makingAnagrams(s1, s2)  # Call the function to get the result

    fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file