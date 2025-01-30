#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Initialize a list to count the occurrences of each letter
    count = []
    for i in range(26):
        count.append(0)
        
    n = len(b)  # Get the length of the input string
    allhappy = True  # Flag to check if all ladybugs are happy
    under = False  # Flag to check if there is any underscore ('_')
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # List of uppercase letters
    
    # Loop through each character in the string
    for i in range(n):
        if b[i] == '_':  # If the character is an underscore
            under = True  # Set the flag to True
        else:
            count[alphabet.find(b[i])] += 1  # Count occurrences of each letter
            
        # Check for special edge cases (n == 1 or mismatch on boundaries)
        if n == 1:
            allhappy = False  # If the string length is 1, it's not happy
        elif i == 0 and b[0] != b[1]:  # If the first character doesn't match the second
            allhappy = False 
        elif i == n - 1 and b[i] != b[i - 1]:  # If the last character doesn't match the previous
            allhappy = False
        elif b[i] != b[i - 1] and b[i] != b[i + 1]:  # If a character doesn't match both neighbors
            allhappy = False
    
    # Check if all ladybugs are happy
    if allhappy:
        return "YES"
    elif 1 not in count and under:  # If no letter has exactly 1 occurrence and there is an underscore
        return "YES"  # It's possible to swap ladybugs to make them happy
    else:
        return "NO"  # Otherwise, it's not possible to make all ladybugs happy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())  # Read the number of test cases

    for g_itr in range(g):
        n = int(input().strip())  # Read the length of the string

        b = input()  # Read the string of ladybugs

        result = happyLadybugs(b)  # Call the function to check if ladybugs can be happy

        fptr.write(result + '\n')  # Write the result to the output file

    fptr.close()