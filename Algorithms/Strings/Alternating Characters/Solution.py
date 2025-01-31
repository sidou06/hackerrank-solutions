#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    let1 = s[0]  # Initialize the first character
    dell  = 0  # Initialize the deletion counter
    for i in range(1, len(s)):  # Iterate through the string starting from the second character
        if s[i] == let1:  # If the current character matches the previous one, increment deletion counter
            dell  += 1
        else:
            if let1 == 'A':  # If the previous character was 'A', change it to 'B'
                let1 = 'B'
            else:
                let1 = 'A'  # Otherwise, change it to 'A'
    return dell  # Return the total number of deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())  # Read the number of test cases

    for q_itr in range(q):
        s = input()  # Read the string for each test case

        result = alternatingCharacters(s)  # Call the function to compute the result

        fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file