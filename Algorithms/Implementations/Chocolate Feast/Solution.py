#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # Calculate how many chocolates can be bought initially with the given money
    nb = n // c
    w = nb  # Store the number of chocolates as w
    while w >= m:
        # Calculate how many more chocolates can be obtained by trading wrappers
        c = w // m
        r = w % m  # Calculate the remaining wrappers
        nb += c  # Add the new chocolates to the total count
        w = r + c  # Update the number of wrappers to the remaining plus the new ones
    return nb  # Return the total number of chocolates

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        # Read input for each test case
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])  # Total money available
        c = int(first_multiple_input[1])  # Cost of one chocolate
        m = int(first_multiple_input[2])  # Number of wrappers required for one free chocolate

        # Call the function to compute the result
        result = chocolateFeast(n, c, m)

        # Write the result to the output file
        fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()