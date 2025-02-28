#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#

def solve(coordinates):
    # Initialize min and max values for x and y coordinates
    minx = 0
    maxx = 0
    miny = 0
    maxy = 0
    
    # Iterate through the list of coordinates to find min/max values
    for i in range(len(coordinates)):
        if coordinates[i][0] > maxx:
            maxx = coordinates[i][0]
        if coordinates[i][0] < minx:
            minx = coordinates[i][0]
        if coordinates[i][1] > maxy:
            maxy = coordinates[i][1]
        if coordinates[i][1] < miny:
            miny = coordinates[i][1]    
    
    # Calculate the distances in x and y directions
    dist1 = maxx - minx
    dist2 = maxy - miny
    
    # Calculate the diagonal distance from the farthest points
    dist3 = math.sqrt((max(abs(maxx), abs(minx))) ** 2 + (max(abs(maxy), abs(miny))) ** 2)
    
    # Return the maximum distance found
    return max(dist1, dist2, dist3)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of coordinates
    n = int(input().strip())

    coordinates = []

    # Read the coordinates into a list
    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    # Compute the result using the solve function
    result = solve(coordinates)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    fptr.close()