#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    # Check if the total sum of the elements in B is odd
    if sum(B) % 2 == 1:
        return 'NO'  # If the sum is odd, it's not possible to divide evenly, return 'NO'
    else:
        i = 0
        aj = 0  # This variable will store the number of operations
        while i < len(B):  # Iterate through the array
            # Skip over all even numbers
            while i < len(B) and B[i] % 2 == 0:
                i += 1
            # If an odd number is found
            if i < len(B):
                aj += 2  # Increase the operation count by 2 (because we're giving out 1 unit to two people)
                i += 1  # Move to the next element
                # Continue with the even numbers
                while i < len(B) and B[i] % 2 == 0:
                    aj += 2  # Again, we add 1 unit to two people, so 2 operations
                    i = i + 1  # Move to the next element
                i += 1  # Continue to the next element
        return str(aj)  # Return the total number of operations as a string
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of elements in the list
    N = int(input().strip())

    # Read the list of integers
    B = list(map(int, input().rstrip().split()))

    # Call the function to calculate the result
    result = fairRations(B)

    # Write the result to the output file
    fptr.write(result + '\n')

    fptr.close()