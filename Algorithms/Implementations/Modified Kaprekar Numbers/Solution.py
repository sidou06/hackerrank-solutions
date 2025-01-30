#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekar(x):
    # Find the number of digits in x
    d = len(str(x))
    # Square the number and convert it to string
    ch = str(x ** 2)
    # Find the number of digits in the left part of the square
    rest = len(ch) - d 
    # Extract the right part of the square
    p1 = int(ch[-d:])
    # Extract the left part of the square or set it to 0 if there is no left part
    p2 = int(ch[:rest]) if rest > 0 else 0
    # Check if the sum of the two parts equals the original number
    return p1 + p2 == x

def kaprekarNumbers(p, q):
    # Write your code here
    # Initialize a flag to check if any valid number is found
    noth = True
    # Initialize a string to store the valid Kaprekar numbers
    arr = ''
    # Loop through the range from p to q
    for i in range(p, q + 1):
        # Check if the number is a Kaprekar number
        if kaprekar(i):
            # Set the flag to False since we found at least one valid number
            noth = False
            # Append the valid number to the result string
            arr += str(i)
            arr += ' '
    # If no valid number is found, print 'INVALID RANGE'
    if noth:
        print('INVALID RANGE')
    else:
        # Otherwise, print the valid numbers
        t = len(arr)
        print(arr[:t])

if __name__ == '__main__':
    # Read the lower bound of the range
    p = int(input().strip())

    # Read the upper bound of the range
    q = int(input().strip())

    # Call the function to print the Kaprekar numbers in the range
    kaprekarNumbers(p, q)