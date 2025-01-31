#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    # Write your code here
    i = 0  # Initialize the index to 0
    count = 0  # Initialize the count of "010" patterns
    while i < len(b) - 2:  # Loop through the string, ensuring there are at least 3 characters left to check
        if b[i] == '0' and b[i + 1] == '1' and b[i + 2] == '0':  # Check for the "010" pattern
            count += 1  # Increment the count when "010" is found
            i += 3  # Skip past the "010" pattern
        else:
            i += 1  # Move to the next character if the pattern is not found
    return count  # Return the count of "010" patterns

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read the length of the string (not used in the logic)

    b = input()  # Read the binary string

    result = beautifulBinaryString(b)  # Call the function to compute the result

    fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file