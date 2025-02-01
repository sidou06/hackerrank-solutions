#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    # If the cost of building a library is less than or equal to the cost of building a road, build a library in each city
    if c_lib <= c_road:
        return c_lib * n

    # Create a graph with cities as nodes and roads as edges
    graph = {node : set() for node in range(1, n + 1)}
    for city_from, city_to in cities:
        graph[city_from].add(city_to)
        graph[city_to].add(city_from)

    nb_villages = 0  # To count the number of disconnected components (villages)
    visited = set()  # To track visited cities

    # Depth-First Search (DFS) to visit all cities in a connected component
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Count the number of connected components (villages)
    for node in range(1, n + 1):
        if node not in visited:
            nb_villages += 1  # A new village found
            dfs(node)  # Visit all cities in this village

    # Calculate the cost: build libraries for each village and roads for cities within each village
    return nb_villages * c_lib + (n - nb_villages) * c_road

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())  # Number of queries

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])  # Number of cities (nodes)
        m = int(first_multiple_input[1])  # Number of roads (edges)
        c_lib = int(first_multiple_input[2])  # Cost of building a library
        c_road = int(first_multiple_input[3])  # Cost of building a road

        cities = []  # List of roads (edges)
        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))  # Add each road

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()