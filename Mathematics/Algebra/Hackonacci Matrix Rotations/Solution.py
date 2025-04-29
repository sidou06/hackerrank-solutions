#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # Read input for grid size and number of queries
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    # Define even numbers for checking
    even = [2, 4, 5]

    # Initialize the main grid 'liste' with values 'X' and 'Y'
    liste = []
    for i in range(n):
        liste.append([])
        for j in range(n):
            # Calculate the result of the condition and append 'X' or 'Y' accordingly
            re = (((i + 1) * (j + 1)) ** 2) % 7
            if re in even:
                liste[i].append('X')
            else:
                liste[i].append('Y')

    # Create rotated grids based on original 'liste'
    liste2 = [[liste[j][i] for j in range(n)] for i in range(n)]
    liste22 = [row[::-1] for row in liste2]
    liste3 = [[liste22[j][i] for j in range(n)] for i in range(n)]
    liste33 = [row[::-1] for row in liste3]

    liste4 = [[liste33[j][i] for j in range(n)] for i in range(n)]
    liste44 = [row[::-1] for row in liste4]

    # Count differences between original grid and its rotated versions
    une = 0
    deux = 0
    trois = 0
    for i in range(n):
        for j in range(n):
            if liste22[i][j] != liste[i][j]:
                une += 1
            if liste33[i][j] != liste[i][j]:
                deux += 1
            if liste44[i][j] != liste[i][j]:
                trois += 1

    # Process queries based on the angle of rotation
    for q_itr in range(q):
        angle = int(input().strip())
        angle = angle % 360
        if angle == 0:
            print(0)
        elif angle == 90:
            print(une)
        elif angle == 180:
            print(deux)
        elif angle == 270:
            print(trois)