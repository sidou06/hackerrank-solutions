#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY dates as parameter.
#

def verif_date(m, d):
    # Checks if both digits of the day (d) are less than the month (m)
    if d % 10 < m and d // 10 < m:
        return True 
    else:
        return False 

def transform_date(m, d):
    # Transforms the date into a unique number based on the month (m) and day (d)
    return d % 10 + (d // 10) * m 

def solve(dates):
    # Dictionary to store transformed date occurrences
    dict = {}
    tot = 0 
    
    # Iterate through the list of dates
    for date in dates:
        if verif_date(date[0], date[1]):  # Check if the date meets the condition
            nb = transform_date(date[0], date[1])  # Transform the date
            if nb in dict:
                dict[nb] += 1  # Increment count if already present
            else:
                dict[nb] = 1  # Initialize count if not present
    
    # Calculate the number of valid date pairs
    for ele in dict:
        a = dict[ele] 
        tot += (a * (a - 1)) // 2  # Compute pair count using nC2 formula
    
    return tot 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of dates
    n = int(input().strip())

    dates = []

    # Read the dates into a list
    for _ in range(n):
        dates.append(list(map(int, input().rstrip().split())))

    # Compute the result using the solve function
    result = solve(dates)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    fptr.close()