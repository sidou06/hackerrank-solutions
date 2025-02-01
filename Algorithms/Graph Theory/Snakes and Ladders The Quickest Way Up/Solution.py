#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

def quickestWayUp(ladders, snakes):
    # Write your code here
    ladders = {ladders[i][0] : ladders[i][1] for i in range(len(ladders))}  # Convert ladder list to dictionary
    snakes = {snakes[i][0] : snakes[i][1] for i in range(len(snakes))}  # Convert snake list to dictionary
    graph = {cell : set() for cell in range(1,100)}  # Initialize graph for each cell
    for cell in graph:  # Iterate through each cell
        for dice in range(1,7):  # Simulate dice roll (1 to 6)
            result = cell + dice  # Calculate the new cell after dice roll
            if result in ladders:  # If there's a ladder, move to the top
                result = ladders[result]
            if result in snakes:  # If there's a snake, move to the bottom
                result = snakes[result]
            if result < 101:  # Ensure the result is within the board
                graph[cell].add(result)  # Add the result as a neighbor in the graph
    depth = {cell : -1 for cell in range(1,101)}  # Initialize depth array for each cell
    depth[1] = 0  # Starting point (cell 1) has depth 0
    queue = deque([1])  # Initialize queue with the starting cell
    while queue:  # BFS to find the shortest path
        cell = queue.popleft()  # Dequeue the current cell
        if cell == 100:  # If we reach cell 100, return the depth
            return depth[cell]
        for neighbor in graph[cell]:  # Iterate through neighbors of the current cell
            if depth[neighbor] == -1:  # If the neighbor hasn't been visited
                depth[neighbor] = depth[cell] + 1  # Update the depth of the neighbor
                queue.append(neighbor)  # Enqueue the neighbor
    return -1  # If it's not possible to reach cell 100, return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open the output file

    t = int(input().strip())  # Read the number of test cases

    for t_itr in range(t):  # Loop through each test case
        n = int(input().strip())  # Read the number of ladders

        ladders = []  # Initialize the ladders list

        for _ in range(n):  # Read the ladders
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())  # Read the number of snakes

        snakes = []  # Initialize the snakes list

        for _ in range(m):  # Read the snakes
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)  # Call the function to find the quickest way up

        fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file