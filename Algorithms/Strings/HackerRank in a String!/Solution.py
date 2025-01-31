#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    # Store the input string in a variable
    sen = s 
    # Default result is "YES"
    res = 'YES'
    # Target word to search in sequence
    word = 'hackerrank'
    # Index to track characters in the target word
    i = 0

    # Iterate through the target word
    while i < 10 and res == 'YES':
        # Check if the current character of the target word is in the remaining string
        if word[i] in sen:
            # Find the position of the character in the remaining string
            pos = sen.index(word[i])
            # Update the remaining string from the next position
            if pos < len(sen) - 1:
                sen = sen[pos + 1:]
            else:
                sen = ''
            # Move to the next character in the target word
            i += 1
        else:
            # If any character is missing, set result to "NO"
            res = 'NO'
    
    return res  # Return the result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())  # Read the number of queries

    for q_itr in range(q):
        s = input()  # Read the input string

        result = hackerrankInString(s)  # Call the function

        fptr.write(result + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file