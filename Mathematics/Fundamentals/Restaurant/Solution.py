#!/bin/python3

import math
import os
import sys

#
# Complete the 'restaurant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER b
#

def PGCD(a, b):
    # Iterate from min(a, b) down to 1 to find the greatest common divisor
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i 

def restaurant(l, b):
    # Calculate the maximum number of square pieces that can be cut
    return (l * b) // ((PGCD(l, b)) ** 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read the number of test cases

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])  # Read length of the rectangle
        b = int(first_multiple_input[1])  # Read breadth of the rectangle

        result = restaurant(l, b)  # Compute the result

        fptr.write(str(result) + '\n')  # Write the result to output file

    fptr.close()  # Close the output file