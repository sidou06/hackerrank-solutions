#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

def saveThePrisoner(n, m, s):
    # The core logic of the problem: calculating the position of the last prisoner
    # (the prisoner who gets the last candy).
    # - m % n gives the remainder after dividing the total candies by the number of prisoners.
    # - We subtract 1 from s to account for the fact that the count starts from prisoner 's'.
    # - The modulo operation ensures that if the number exceeds 'n' (i.e., it wraps around), 
    #   the count starts from the first prisoner again.

    x = ((m % n) + s - 1) % n  # Calculate the final position after distributing all candies.
    
    # If x is 0, it means the last candy goes to the nth prisoner.
    if x == 0:
        return n
    else:
        return x  # Return the position of the last prisoner.

if __name__ == '__main__':
    # Open the output file to write the result.
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input value for t (number of test cases).
    t = int(input().strip())

    # Loop through each test case.
    for t_itr in range(t):
        # Read n, m, s values for each test case.
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])  # Number of prisoners
        m = int(first_multiple_input[1])  # Number of candies
        s = int(first_multiple_input[2])  # Starting prisoner number

        # Call the saveThePrisoner function and get the result.
        result = saveThePrisoner(n, m, s)

        # Write the result to the output file.
        fptr.write(str(result) + '\n')

    # Close the output file after writing the results.
    fptr.close()












