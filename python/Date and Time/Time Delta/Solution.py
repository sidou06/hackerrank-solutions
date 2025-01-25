#!/bin/python3

import os
from dateutil import parser

# Complete the time_delta function below.
def time_delta(t1, t2):
    # Parse the input timestamps
    d1 = parser.parse(t1)
    d2 = parser.parse(t2)
    # Calculate the difference in seconds
    d = d1 - d2
    return str(abs(int(d.total_seconds())))

if __name__ == '__main__':
    # Open output file
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Number of test cases
    t = int(input())

    for _ in range(t):
        # Input timestamps
        t1 = input()
        t2 = input()

        # Calculate the time difference
        delta = time_delta(t1, t2)

        # Write the result to the output file
        fptr.write(delta + '\n')

    # Close the file
    fptr.close()