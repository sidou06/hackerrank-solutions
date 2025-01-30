#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Convert the integer n to a string for easier digit iteration
    ch = str(n)
    res = 0
    # Iterate through each digit of the number
    for c in ch:
        # Ensure the digit is not zero and check if it divides n
        if int(c) != 0 and n % int(c) == 0:
            res += 1
    # Return the count of digits that divide n
    return res

if __name__ == '__main__':
    # Open the output file to write the result.
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases.
    t = int(input().strip())

    # For each test case, read the number n and compute the result.
    for t_itr in range(t):
        n = int(input().strip())

        # Call the findDigits function and get the result.
        result = findDigits(n)

        # Write the result to the output file.
        fptr.write(str(result) + '\n')

    # Close the output file after writing the results.
    fptr.close()