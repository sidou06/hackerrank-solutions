#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Initialize a counter for altered characters
    nb = 0
    
    # Iterate over each character in the string
    for i in range(len(s)):
        # Check if the character at index i is incorrect based on the repeating pattern "SOS"
        if (i % 3 == 0 or i % 3 == 2) and s[i] != 'S':
            nb += 1  # Increment counter if expected 'S' is different
        if i % 3 == 1 and s[i] != 'O':
            nb += 1  # Increment counter if expected 'O' is different
    
    return nb  # Return the total number of altered characters

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()  # Read the input string

    result = marsExploration(s)  # Call the function to count altered characters

    fptr.write(str(result) + '\n')  # Write the result to output file

    fptr.close()  # Close the output file