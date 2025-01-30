#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

def taumBday(b, w, bc, wc, z):
    # Calculate the cost for each scenario and return the minimum cost
    if bc + z < wc:
        return bc * b + (bc + z) * w  # Buying black gifts with the conversion cost for white
    elif wc + z < bc:
        return wc * w + (wc + z) * b  # Buying white gifts with the conversion cost for black
    else:
        return bc * b + wc * w  # Buying gifts at their respective prices without conversion

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read the number of test cases

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])  # Number of black gifts
        w = int(first_multiple_input[1])  # Number of white gifts

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])  # Cost of a black gift
        wc = int(second_multiple_input[1])  # Cost of a white gift
        z = int(second_multiple_input[2])  # Cost to convert one gift from black to white or vice versa

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')  # Write the result for the current test case

    fptr.close()