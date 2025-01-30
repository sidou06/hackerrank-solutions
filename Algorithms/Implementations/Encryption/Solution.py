#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Remove spaces from the input string
    s = s.replace(" ", "")
    
    # Calculate the square root of the length of the string
    l = len(s)
    r = int(math.sqrt(l))
    c = r
    
    # Adjust the rows and columns if necessary
    if r * c < l:
        c += 1
    if r * c < l:
        r += 1
    
    # Prepare the result string
    res = ""
    
    # Create the encrypted string by traversing the string column by column
    for row in range(c):
        col = 0
        while col < r and col * c + row < l:
            res += s[col * c + row]
            col += 1
        res += " "
    
    # Remove the trailing space and return the result
    return res[:-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()  # Read the input string

    result = encryption(s)  # Call the encryption function

    fptr.write(result + '\n')  # Write the result to the output

    fptr.close()