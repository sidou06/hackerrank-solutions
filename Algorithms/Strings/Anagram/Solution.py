#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    count = -1
    l = len(s)
    if l % 2 == 0:  # If the string has an even length
        count = 0
        s1 = s[:l // 2]  # First half of the string
        s2 = s[l // 2:]  # Second half of the string
        for c in s1:
            if c in s2:
                ind = s2.index(c)  # Find the character in the second half
                s2 = s2[:ind] + s2[ind + 1:]  # Remove the matched character from s2
            else:
                count += 1  # If no match is found, increment the count
    return count  # Return the count of characters to remove to make the string an anagram

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())  # Read the number of test cases

    for q_itr in range(q):
        s = input()  # Read the string for each test case

        result = anagram(s)  # Call the function to get the result

        fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file