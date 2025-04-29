#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#

def solve(coordinates):
    # Initialize an empty list to store results
    res = [] 
    
    # Loop through each coordinate pair
    for c in coordinates:
        x = c[0]  # X-coordinate
        y = c[1]  # Y-coordinate
        # Calculate the distance from the origin (0,0) using Pythagorean theorem
        d = math.sqrt(x ** 2 + y ** 2)
        
        # Determine the angle based on the position of the coordinate
        if x == 0:
            if y > 0:
                angle = 90  # Angle for positive Y-axis
            else:
                angle = 270  # Angle for negative Y-axis
        else:
            # Calculate the angle in degrees using arctangent
            angle = math.atan(y/x) * 180 / math.pi 
            
            # Adjust angle depending on the quadrant
            if x > 0 and y < 0:
                angle += 360  # Adjust for quadrant IV
            elif x < 0:
                angle += 180  # Adjust for quadrant II or III
        
        # Append the coordinate and its corresponding angle and distance to the result list
        res.append([[x, y], [angle, d]])
    
    # Sort the list based on angle first, then distance
    resu = sorted(res, key=lambda v: (v[1][0], v[1][1]))
    
    # Extract the coordinates from the sorted result
    f = []
    for r in resu:
        f.append(r[0])
    
    # Return the sorted coordinates based on angle and distance
    return f 

if __name__ == '__main__':
    # Open output file for writing
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values for number of coordinates (n)
    n = int(input().strip())

    # Initialize the list of coordinates (2D array)
    coordinates = []

    # Read the 2D array of coordinates from input
    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    # Get the result from the solve function
    result = solve(coordinates)

    # Write the result to the output file, with space-separated coordinates
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    # Close the output file
    fptr.close()