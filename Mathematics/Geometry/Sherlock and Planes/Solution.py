#!/bin/python3

import math
import os
import random
import re
import sys

# Calculate the determinant of a 3x3 matrix
def det3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

# Calculate the determinant of a 4x4 matrix
def det4(matrix):
    a, b, c, d = matrix[0]
    e, f, g, h = matrix[1]
    i, j, k, l = matrix[2]
    m, n, o, p = matrix[3]

    # Compute the cofactor expansion along the first row
    fi = a * det3([[f, g, h], [j, k, l], [n, o, p]])
    se = b * det3([[e, g, h], [i, k, l], [m, o, p]])
    th = c * det3([[e, f, h], [i, j, l], [m, n, p]])
    fo = d * det3([[e, f, g], [i, j, k], [m, n, o]])

    # Return the determinant
    return fi - se + th - fo

# Check if the 4 points lie on the same plane
def solve(points):
    # Add a 1 as the fourth coordinate to each point
    for i in range(len(points)):
        points[i].append(1)

    # Calculate the determinant
    de = det4(points)

    # If determinant is zero, the points are coplanar
    if de == 0:
        return "YES"
    else:
        return "NO"

# Entry point of the program
if __name__ == '__main__':
    # Open the output file
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of test cases
    t = int(input().strip())

    # Process each test case
    for t_itr in range(t):
        points = []

        # Read 4 points
        for _ in range(4):
            points.append(list(map(int, input().rstrip().split())))

        # Solve for the given set of points
        result = solve(points)

        # Write the result
        fptr.write(result + '\n')

    # Close the output file
    fptr.close()