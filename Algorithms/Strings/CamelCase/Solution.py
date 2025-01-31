#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Initialize the word count to 1, assuming the string is non-empty
    res = 1  
    
    # Iterate through each character in the string
    for ele in s:
        # If the character is uppercase, it indicates a new word in camelCase
        if ele.isupper():
            res += 1  
    
    return res  # Return the total number of words

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()  # Read input string

    result = camelcase(s)  # Call the function

    fptr.write(str(result) + '\n')  # Write the result to output file

    fptr.close()  # Close the output file