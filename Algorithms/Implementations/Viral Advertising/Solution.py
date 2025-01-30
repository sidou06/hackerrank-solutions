#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Initialize the number of people to whom the advertisement is shared on the first day.
    shared = 5
    cumulative = 0  # This will store the total number of people who liked the advertisement.

    # Loop for each day (from 1 to n).
    for i in range(n):
        # Calculate how many people liked the advertisement that day (half of the shared).
        liked = shared // 2
        cumulative = cumulative + liked  # Add the number of people who liked to the cumulative total.
        
        # Update the number of people who will be shared the advertisement on the next day (liked * 3).
        shared = liked * 3

    # Return the total number of likes after n days.
    return cumulative

if __name__ == '__main__':
    # Open the output file to write the result.
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input value for n (number of days).
    n = int(input().strip())

    # Call the viralAdvertising function with n as input and store the result.
    result = viralAdvertising(n)

    # Write the result to the output file.
    fptr.write(str(result) + '\n')

    # Close the output file.
    fptr.close()