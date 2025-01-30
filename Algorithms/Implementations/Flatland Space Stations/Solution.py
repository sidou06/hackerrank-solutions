#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    # Sort the space stations' positions in ascending order
    c.sort()
    
    # Find the maximum distance from the first city to the first station, 
    # and from the last city to the last station
    b = max(c[0], n - c[-1] - 1)
    
    # Check the maximum distance between consecutive space stations
    for i in range(len(c) - 1):
        curr = (c[i + 1] - c[i]) // 2  # Calculate the half distance between two consecutive stations
        b = max(b, curr)  # Update the maximum distance found so far
    
    return b  # Return the maximum distance to the nearest space station

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of cities (n) and number of space stations (m)
    nm = input().split()

    n = int(nm[0])  # Total number of cities
    m = int(nm[1])  # Total number of space stations

    # Read the positions of the space stations
    c = list(map(int, input().rstrip().split()))

    # Call the function to find the largest minimum distance to the nearest space station
    result = flatlandSpaceStations(n, c)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    fptr.close()