#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    # Calculate the distances of each cat from the mouse
    d1 = abs(x - z)
    d2 = abs(y - z)
    
    # Determine which cat gets to the mouse first or if it's a tie
    if d1 > d2:
        return "Cat B"
    elif d2 > d1:
        return "Cat A"
    else:
        return "Mouse C"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    q = int(input())

    # Process each test case
    for q_itr in range(q):
        # Read the positions of the cats and the mouse
        xyz = input().split()

        x = int(xyz[0])  # Position of Cat A
        y = int(xyz[1])  # Position of Cat B
        z = int(xyz[2])  # Position of the Mouse

        # Determine the result for this test case
        result = catAndMouse(x, y, z)

        # Write the result to the output
        fptr.write(result + '\n')

    fptr.close()