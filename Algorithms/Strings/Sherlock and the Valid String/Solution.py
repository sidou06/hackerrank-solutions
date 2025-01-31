#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    counts = []  # List to store the frequency of each character
    letters = []  # List to store the unique characters
    for c in s:
        if c in letters:
            counts[letters.index(c)] += 1  # Increment the count if character is already in letters
        else:
            letters.append(c)  # Add new character to letters
            counts.append(1)  # Initialize count for new character

    prem = counts.count(counts[0])  # Count how many times the first count appears
    l = len(counts)  # Get the length of the counts list

    # Check for cases where all character frequencies are the same
    if prem == l:
        return "YES"
    
    # Check for cases where all but one frequency is the same
    elif prem == l - 1:
        k = 1  # Start checking from the second frequency
        while counts[k] == counts[0]:  # Find the character with a different frequency
            k += 1
        # If the frequency difference is 1 or the character appears once, it's valid
        if counts[k] == 1 or counts[k] - counts[0] == 1:
            return "YES"
        else:
            return "NO"
    
    # Handle cases where the first frequency appears only once
    elif prem == 1:
        if counts.count(counts[1]) == l - 1 and counts[0] - counts[1] == 1:
            return "YES"
        else:
            return "NO"
    
    # If none of the conditions match, return "NO"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open the output file for writing

    s = input()  # Read the input string

    result = isValid(s)  # Call the function to check if the string is valid

    fptr.write(result + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file