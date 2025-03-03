#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pgcd(x, y):
    # Compute the greatest common divisor (GCD) of two numbers using recursion
    s = min(x, y)  # Get the smaller number
    k = max(x, y)  # Get the larger number
    if k % s == 0:
        return s  # If k is divisible by s, return s as the GCD
    else:
        return pgcd(s, k % s)  # Recursively compute the GCD

def solve(a):
    # Iterate through the array to check if the GCD of all elements is 1
    for i in range(len(a)):
        if i == 0:
            p = a[i]  # Initialize GCD with the first element
            if p == 1:
                return "YES"  # If the first element is 1, return "YES" immediately
        else:
            p = pgcd(p, a[i])  # Update GCD with the current element
            if p == 1:
                return "YES"  # If GCD becomes 1 at any point, return "YES"
    
    return "NO"  # If GCD is never 1, return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file for writing

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        a_count = int(input().strip())  # Read number of elements in array

        a = list(map(int, input().rstrip().split()))  # Read the array elements

        result = solve(a)  # Call function to determine result

        fptr.write(result + '\n')  # Write result to output file

    fptr.close()  # Close the output file