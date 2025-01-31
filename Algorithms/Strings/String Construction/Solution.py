#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):
    # Write your code here
    cost = 0  # Initialize the cost variable
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # The alphabet to check for unique characters
    for c in alphabet:  # Loop through each character in the alphabet
        if c in s:  # If the character is found in the string
            cost += 1  # Increment the cost (each unique character adds 1 to the cost)
    return cost  # Return the total cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open the output file for writing

    q = int(input().strip())  # Read the number of test cases

    for q_itr in range(q):  # Iterate through each test case
        s = input()  # Read the input string

        result = stringConstruction(s)  # Call the function to get the cost

        fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file