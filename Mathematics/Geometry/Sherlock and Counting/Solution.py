#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'solve' function below
# The function returns an INTEGER
# The function accepts two INTEGER parameters: n and k
def solve(n, k):
    # Calculate the discriminant of the quadratic inequality
    delta = n * n - 4 * n * k

    # If delta is less than or equal to 0, return n - 1
    if delta <= 0:
        return n - 1
    else:
        # Calculate the lower bound x1
        x1 = int((n - math.sqrt(delta)) / 2)
        # Ensure s1 is not negative
        s1 = max(x1, 0)

        # Calculate the upper bound x2
        x2 = (n + math.sqrt(delta)) / 2
        # Round up if x2 is not an integer
        if int(x2) == x2:
            x2 = int(x2)
        else:
            x2 = int(x2) + 1
        # Ensure s2 is not negative
        s2 = max(n - x2, 0)

        # Return total count of valid values from both sides
        return s1 + s2

# Entry point of the program
if __name__ == '__main__':
    # Open the output file
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of queries
    q = int(input().strip())

    # Process each query
    for q_itr in range(q):
        # Read n and k
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])

        # Get the result for the query
        result = solve(n, k)

        # Write the result to the output file
        fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()