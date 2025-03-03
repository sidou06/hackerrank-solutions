#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER x
#

def closestNumber(a, b, x):
    # Compute a raised to the power of b
    nb = pow(a, b)
    
    # Find the closest multiple of x less than or equal to nb
    d1 = x * (nb // x)
    
    # Find the closest multiple of x greater than nb
    d2 = d1 + x 
    
    # Return the multiple that is closer to nb
    if abs(nb - d1) > abs(nb - d2): 
        return int(d2)
    else:
        return int(d1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file for writing

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])  # Read a
        b = int(first_multiple_input[1])  # Read b
        x = int(first_multiple_input[2])  # Read x

        result = closestNumber(a, b, x)  # Call function

        fptr.write(str(result) + '\n')  # Write result to output file

    fptr.close()  # Close the output file