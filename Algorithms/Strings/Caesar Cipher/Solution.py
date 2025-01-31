#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

# List of lowercase letters
Minin = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# List of uppercase letters
Majis = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def caesarCipher(s, k):
    # Initialize the resulting encrypted string
    new = ''
    
    # Iterate over each character in the input string
    for i in range(len(s)):
        if s[i].isupper():  # Check if the character is uppercase
            j = 0
            found = False  
            while j < 26 and not found:
                if Majis[j] == s[i]:  # Find the character index in the uppercase list
                    new += Majis[(j + k) % 26]  # Shift the character by k positions
                    found = True  
                j += 1
        elif s[i].islower():  # Check if the character is lowercase
            j = 0
            found = False  
            while j < 26 and not found:
                if Minin[j] == s[i]:  # Find the character index in the lowercase list
                    new += Minin[(j + k) % 26]  # Shift the character by k positions
                    found = True
                j += 1
        else:  # If character is not a letter, keep it unchanged
            new += s[i]
    
    return new  # Return the encrypted string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read the length of the string

    s = input()  # Read the input string

    k = int(input().strip())  # Read the shift value

    result = caesarCipher(s, k)  # Encrypt the string using Caesar cipher

    fptr.write(result + '\n')  # Write the encrypted string to output file

    fptr.close()  # Close the output file