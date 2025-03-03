#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'canConstruct' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY a as parameter.
#

def sum_digits(a):
    somme = 0
    ch = str(a)  # Convert the number to a string
    for i in range(len(ch)):
        somme = somme + (a // pow(10,i)) % 10  # Extract each digit and sum them
    return somme 

def canConstruct(a):
    # Return "Yes" or "No" denoting whether you can construct the required number.
    somme = 0  # Initialize sum of digits
    for nb in a:
        somme = somme + sum_digits(nb)  # Sum the digits of all numbers in the list
    if somme % 3 == 0:  # Check if the sum is divisible by 3
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file for writing

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        n = int(input().strip())  # Read the number of elements

        a = list(map(int, input().rstrip().split()))  # Read the list of integers

        result = canConstruct(a)  # Call the function

        fptr.write(result + '\n')  # Write result to output file

    fptr.close()  # Close the output file