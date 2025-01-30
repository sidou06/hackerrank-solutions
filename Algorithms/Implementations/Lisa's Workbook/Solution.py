#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Initialize page number and counters for chapters and special pages
    p = 1  # The current page number
    ch = cpt = 0  # Chapter counter and the count of special pages
    while ch < n:  # Loop over all chapters
        ex = 1  # Exercise counter
        while ex <= arr[ch]:  # Loop over exercises in the current chapter
            if ex == p:  # Check if the exercise number matches the current page number
                cpt += 1  # Increment the count of special pages
            ex += 1  # Move to the next exercise
            if (ex - 1) % k == 0 and ex <= arr[ch]:  # If the current exercise is at the end of a page
                p += 1  # Increment the page number
        p += 1  # Move to the next page after finishing this chapter
        ch += 1  # Move to the next chapter
    
    return cpt  # Return the count of special pages

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the first line input containing n (number of chapters) and k (number of exercises per page)
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])  # Number of chapters
    k = int(first_multiple_input[1])  # Number of exercises per page

    # Read the list of exercises in each chapter
    arr = list(map(int, input().rstrip().split()))

    # Call the function with the inputs and get the result
    result = workbook(n, k, arr)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    fptr.close()