#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Handle years after 1918 (Gregorian calendar)
    if year > 1918:
        # Leap year in the Gregorian calendar
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return "12.09." + str(year)
        else:
            return "13.09." + str(year)
    # Handle years before 1918 (Julian calendar)
    elif year < 1918:
        if year % 4 == 0:
            return "12.09." + str(year)
        else:
            return "13.09." + str(year)
    # Handle the year 1918 (transition year)
    else:
        return "26.09." + str(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input
    year = int(input().strip())

    # Get the result and write it to the output file
    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()