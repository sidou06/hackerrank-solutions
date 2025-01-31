#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Initialize flags for required character types
    up = lo = dig = sp = True  
    
    # Iterate through each character in the password
    for c in password:
        if c.isupper():  # Check if there's an uppercase letter
            up = False  
        elif c.islower():  # Check if there's a lowercase letter
            lo = False  
        elif c.isdigit():  # Check if there's a digit
            dig = False  
        else:  # If not any of the above, it's a special character
            sp = False  
    
    # Return the maximum of the missing character types or the required length difference
    return max(up + lo + dig + sp, 6 - len(password))  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read the length of the password

    password = input()  # Read the password

    answer = minimumNumber(n, password)  # Compute the minimum characters needed

    fptr.write(str(answer) + '\n')  # Write the result to output file

    fptr.close()  # Close the output file