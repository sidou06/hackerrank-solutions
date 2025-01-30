#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # List of words for numbers
    Numbers = ["o' clock",'one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','quarter','sixteen','seventeen','eighteen','nineteen','twenty','twenty one','twenty two','twenty three','twenty four','twenty five','twenty six','twenty seven','twenty eight','twenty nine','half']
    
    # Define the appropriate label for minutes
    if m == 1 or m == 59:
        mi = 'minute '
    elif m == 15 or m == 30 or m == 45:
        mi = ''
    else:
        mi = 'minutes '    
    
    # If minutes is 0, it's an exact hour
    if m == 0:
        return Numbers[h] + ' ' + Numbers[m]
    
    # If minutes is less than or equal to 30, it is "past"
    elif m <= 30:
        return Numbers[m] + ' ' + mi + 'past ' + Numbers[h]
    
    # If minutes is greater than 30, it is "to" the next hour
    else:
        return Numbers[60 - m] + ' ' + mi + 'to ' + Numbers[h + 1]

if __name__ == '__main__':
    # Open the output file for writing the result
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input values
    h = int(input().strip())
    m = int(input().strip())

    # Call the function to convert the time to words
    result = timeInWords(h, m)

    # Write the result to the output file
    fptr.write(result + '\n')

    # Close the output file
    fptr.close()