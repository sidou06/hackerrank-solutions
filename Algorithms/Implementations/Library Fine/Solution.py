#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Initialize fine to 0
    fine = 0
    
    # Check if the book is returned after the due year
    if y1 > y2:
        fine = 10000
    # If the book is returned in the same year, check for the month
    elif y1 == y2 and m1 > m2:
        fine = 500 * (m1 - m2)  # Fine is 500 for each month overdue
    # If the book is returned in the same month and year, check for the day
    elif y1 == y2 and m1 == m2 and d1 > d2:
        fine = 15 * (d1 - d2)  # Fine is 15 for each day overdue
    return fine

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input for the first date (actual return date)
    first_multiple_input = input().rstrip().split()
    d1 = int(first_multiple_input[0])
    m1 = int(first_multiple_input[1])
    y1 = int(first_multiple_input[2])

    # Read input for the second date (due date)
    second_multiple_input = input().rstrip().split()
    d2 = int(second_multiple_input[0])
    m2 = int(second_multiple_input[1])
    y2 = int(second_multiple_input[2])

    # Call the libraryFine function to calculate the fine
    result = libraryFine(d1, m1, y1, d2, m2, y2)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()