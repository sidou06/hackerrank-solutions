#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    h = s[0:2]  # Extract hours
    m = s[3:5]  # Extract minutes
    se = s[6:8]  # Extract seconds
    if s[8:10] == 'PM' and int(h) < 12:
        s = str(int(h)+12) + ':' + m + ':' + se  # Convert to 24-hour format if PM
    elif s[8:10] == 'AM' and int(h) == 12:
        s = '00' + ':' + m + ':' + se  # Handle 12 AM case
    else:
        s = h + ':' + m + ':' + se  # If no change needed, return the time as is
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open the output file

    s = input()  # Read input time

    result = timeConversion(s)  # Call the function to convert time

    fptr.write(result + '\n')  # Write the result to the output file

    fptr.close()  # Close the file