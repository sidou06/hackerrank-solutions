#!/bin/python3

import math
import os
import random
import re
import sys

# Entry point of the program
if __name__ == '__main__':
    # Read the number of points
    n = int(input())

    # Initialize a list to store the coordinates of the points
    points = []

    # Loop to read all points
    for n_itr in range(n):
        # Read x and y as strings, then convert to integers
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
        # Append the point as a list [x, y]
        points.append([x, y])

    # Initialize flags to check horizontal (same y) and vertical (same x) alignment
    h = True
    v = True

    # Start checking from the second point
    i = 1

    # Store the x and y of the first point for comparison
    lv = points[0][0]  # reference x value
    lh = points[0][1]  # reference y value

    # Loop through the remaining points
    while i < len(points) and (h == True or v == True):
        # If x differs from the first point's x, it's not vertical
        if points[i][0] != lv:
            v = False
        # If y differs from the first point's y, it's not horizontal
        if points[i][1] != lh:
            h = False
        # Move to the next point
        i += 1

    # If either all x or all y are the same, print YES, else print NO
    if h == True or v == True:
        print("YES")
    else:
        print("NO")