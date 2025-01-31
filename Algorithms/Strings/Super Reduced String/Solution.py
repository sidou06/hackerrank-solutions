#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Convert the input string into a list for easy modification
    nbop = 1  # Variable to track the number of operations performed
    li = list(s)  # Convert the string to a list
    j = 0  # Initialize the index

    # Continue looping as long as there are adjacent duplicate characters to remove
    while nbop > 0:
        nbop = 0  # Reset operation count
        j = 0  # Reset index
        
        # Iterate through the list to check for adjacent duplicate characters
        while j < len(li) - 1:
            if li[j] == li[j + 1]:  # If two consecutive characters are the same
                nbop += 1  # Increment operation count
                li.pop(j)  # Remove the first character
                li.pop(j)  # Remove the second character (same index as the first removed)
            else:
                j = j + 1  # Move to the next index

    # Convert the modified list back to a string
    res = "".join(li)  
    
    # If the resulting string is empty, return "Empty String"
    if res == "":
        res = "Empty String"
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()  # Read input string

    result = superReducedString(s)  # Call the function

    fptr.write(result + '\n')  # Write the result to output file

    fptr.close()  # Close the output file