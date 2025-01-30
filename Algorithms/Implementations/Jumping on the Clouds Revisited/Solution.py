#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    # Initialize the energy at 100, and the initial position at 0
    energy = 100
    pos = 0
    
    # Continue jumping until we return to the starting position
    while (pos + k) % len(c) != 0:
        # Update the position after each jump
        pos = (pos + k) % len(c)
        # Decrease energy by 1 for each jump
        energy -= 1
        # If the cloud is a thundercloud (1), decrease energy by 2 more
        if c[pos] == 1:
            energy -= 2
    
    # Final jump to return to the starting cloud, decrease energy by 1
    energy -= 1
    
    # If the starting cloud was a thundercloud, decrease energy by 2 more
    if c[0] == 1:
        energy -= 2
    
    # Return the remaining energy
    return energy

if __name__ == '__main__':
    # Open the output file to write the result.
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input values: n (number of clouds) and k (jump length).
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    # Read the cloud configuration: 0 for a normal cloud, 1 for a thundercloud.
    c = list(map(int, input().rstrip().split()))

    # Call the jumpingOnClouds function and get the result.
    result = jumpingOnClouds(c, k)

    # Write the result to the output file.
    fptr.write(str(result) + '\n')

    # Close the output file after writing the results.
    fptr.close()