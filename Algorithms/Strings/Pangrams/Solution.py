#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Initialize result as "pangram"
    res = "pangram"
    # Define the alphabet string
    alp = "abcdefghijklmnopqrstuvwxyz"
    # Index to track letters
    i = 0 

    # Check if all letters of the alphabet are present in the string
    while i < 26 and res == "pangram":
        # Check both lowercase and uppercase versions of the letter
        if alp[i] in s or alp[i].upper() in s:
            i += 1
        else:
            # If any letter is missing, set result to "not pangram"
            res = "not pangram" 
    
    return res  # Return the result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()  # Read input string

    result = pangrams(s)  # Call function

    fptr.write(result + '\n')  # Write result to output file

    fptr.close()  # Close the output file