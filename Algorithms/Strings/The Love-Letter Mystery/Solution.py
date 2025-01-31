#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    # Write your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # Define the alphabet
    count = 0  # Initialize the count of changes required
    for i in range(len(s) // 2):  # Loop through the first half of the string
        # Calculate the difference between the letters in the corresponding positions
        count += abs(alphabet.index(s[i]) - alphabet.index(s[len(s) - i - 1])) 
    return count  # Return the total count of changes needed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())  # Read the number of test cases

    for q_itr in range(q):
        s = input()  # Read the string for each test case

        result = theLoveLetterMystery(s)  # Call the function to calculate the result

        fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file