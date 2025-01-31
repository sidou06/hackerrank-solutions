#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'morganAndString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def morganAndString(a, b):
    # Add a dummy character to handle edge cases
    a += "z"
    b += "z"
    sol = ""
    
    # Merge the two strings in lexicographical order
    for _ in range(len(a) + len(b) - 2):   
        if a < b:
            sol += a[0]
            a = a[1:]  # Remove the first character
        else:
            sol += b[0]
            b = b[1:]  # Remove the first character
            
    return sol  # Return the merged string
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Number of test cases

    for t_itr in range(t):
        a = input()  # Input string a

        b = input()  # Input string b

        result = morganAndString(a, b)  # Call the function to merge strings

        fptr.write(result + '\n')  # Write the result to the output file

    fptr.close()