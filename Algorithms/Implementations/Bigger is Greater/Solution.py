#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Find the first character that is smaller than its next character when traversing from the right
    i = len(w) - 1
    while i > 0 and w[i-1] >= w[i]:
        i -= 1
    
    # If no such character is found, return "no answer"
    if i == 0:
        return "no answer"
    
    # Find the smallest character on the right side of w[i-1] that is larger than w[i-1]
    j = len(w) - 1
    while w[j] <= w[i-1]:
        j -= 1
    
    # Swap the characters
    w = list(w)
    w[i-1], w[j] = w[j], w[i-1]
    
    # Reverse the substring after w[i-1]
    w = w[:i] + w[i:][::-1]
    
    return ''.join(w)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())  # Read the number of test cases

    for T_itr in range(T):
        w = input()  # Read the input word

        result = biggerIsGreater(w)  # Call the function to get the next greater word

        fptr.write(result + '\n')  # Write the result to the output

    fptr.close()