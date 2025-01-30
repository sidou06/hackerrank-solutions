#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    # Initialize a list to store the layers of the matrix
    layers = []
    l = len(matrix)  # Number of rows in the matrix
    c = len(matrix[0])  # Number of columns in the matrix
    
    # Calculate the number of layers (half of the smaller dimension)
    nb_layers = min(l,c) // 2
    
    # Extract each layer from the matrix
    for i in range(nb_layers):
        current_layer = []
        
        # Traverse the left side of the current layer
        for j in range(i, l - i):
            current_layer.append(matrix[j][i])
        
        # Traverse the bottom side of the current layer
        for j in range(i + 1, c - 1 - i):
            current_layer.append(matrix[l - 1 - i][j])
        
        # Traverse the right side of the current layer
        for j in range(l - 1 - i, i - 1, -1):
            current_layer.append(matrix[j][c - 1 - i])
        
        # Traverse the top side of the current layer
        for j in range(c - 2 - i, i, -1):
            current_layer.append(matrix[i][j])
        
        # Store the layer
        layers.append(current_layer)
    
    # Rotate each layer by the given number of rotations
    for i in range(nb_layers):
        current_mod = len(layers[i])  # Length of the current layer
        idx = (-1 * r) % current_mod  # Find the starting index after rotation
        
        # Update the matrix with the rotated values for the current layer
        for j in range(i, l - i):
            matrix[j][i] = layers[i][idx]
            idx = (idx + 1) % current_mod
        
        for j in range(i + 1, c - 1 - i):
            matrix[l - 1 - i][j] = layers[i][idx]
            idx = (idx + 1) % current_mod
        
        for j in range(l - 1 - i, i - 1, -1):
            matrix[j][c - 1 - i] = layers[i][idx]
            idx = (idx + 1) % current_mod
        
        for j in range(c - 2 - i, i, -1):
            matrix[i][j] = layers[i][idx]
            idx = (idx + 1) % current_mod
    
    # Print the rotated matrix
    for row in matrix:
        print(" ".join(str(x) for x in row))
                
    return

if __name__ == '__main__':
    # Read input values for matrix dimensions and rotations
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])  # Number of rows
    n = int(first_multiple_input[1])  # Number of columns
    r = int(first_multiple_input[2])  # Number of rotations

    # Read the matrix data
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    # Perform the matrix rotation
    matrixRotation(matrix, r)