#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    nbs = []  # List to store the index positions of characters in alphabet
    diff = []  # List to store the differences between consecutive character indices
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # Alphabet to compare character positions

    # Convert characters in string to their respective positions in the alphabet
    for let in s:
        nbs.append(alphabet.index(let))

    # Calculate the differences between consecutive character positions
    for i in range(len(nbs) - 1):
        diff.append(abs(nbs[i] - nbs[i + 1]))

    i = 0
    funny = True  # Flag to determine if the string is funny or not

    # Compare the differences from both ends of the string
    while  i < len(diff) // 2 and funny:
        if diff[i] != diff[-(i + 1)]:
            funny = False  # If any difference does not match, set funny to False
        i += 1

    # Return "Funny" or "Not Funny" based on the comparison result
    if funny:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())  # Read the number of test cases

    for q_itr in range(q):
        s = input()  # Read the string input

        result = funnyString(s)  # Call the funnyString function

        fptr.write(result + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file