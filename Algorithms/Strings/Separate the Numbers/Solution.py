#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

# Helper function to check if numbers form a consecutive sequence
def starting(s,first):
    while s:
        if s.startswith(first):
            s = s[len(first):]  # Remove the current number from the string
            first = str(int(first) + 1)  # Increment the number for the next check
        else:
            return False  # Return False if sequence is broken
    return True  # Return True if the entire string is processed correctly

def separateNumbers(s):
    # Check if the string starts with "0" and has more than one character
    if s[0] == "0" and len(s) > 1:
        print("NO")  # It's not possible to form a sequence
        return None 

    # Iterate through possible lengths of the first number in the sequence
    for i in range(1, len(s) // 2 + 1):
        first = s[:i]  # Extract the first number as a string
        if starting(s, first):  # Check if the string can form a valid sequence
            print("YES", first)  # Print YES and the first number
            return None 

    # If no valid sequence is found, print NO
    print("NO")
    return None 

if __name__ == '__main__':
    q = int(input().strip())  # Read the number of test cases

    # Process each test case
    for q_itr in range(q):
        s = input()  # Read the input string
        separateNumbers(s)  # Call the function to check the sequence