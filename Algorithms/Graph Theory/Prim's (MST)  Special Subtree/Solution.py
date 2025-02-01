#!/bin/python3

import math
import os
import random
import re
import sys
import heapq 

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, edges, start):
    graph = {}  # Initialize an empty graph
    for edge in edges:  # Loop through each edge
        if edge[0] in graph:  # If the node exists in the graph, append the edge
            graph[edge[0]].append([edge[1], edge[2]])
        else:
            graph[edge[0]] = [[edge[1], edge[2]]]  # Otherwise, create a new list of edges for the node
        if edge[1] in graph:  # Same for the reverse edge
            graph[edge[1]].append([edge[0], edge[2]])
        else:
            graph[edge[1]] = [[edge[0], edge[2]]]
    
    visited = set()  # Set to track visited nodes
    min_heap = [(0, start, None)]  # (weight, current_node, previous_node) - start with 0 weight
    total_cost = 0  # Initialize total cost of the minimum spanning tree

    while min_heap:  # While there are edges in the priority queue
        weight, current_node, previous_node = heapq.heappop(min_heap)  # Pop the edge with the smallest weight
        if current_node not in visited:  # If the node hasn't been visited yet
            visited.add(current_node)  # Mark the node as visited
            total_cost += weight  # Add the weight of the edge to the total cost
            print(total_cost)  # Print the current total cost for debugging
            print(visited)  # Print the visited nodes for debugging

            for neighbor, edge_weight in graph[current_node]:  # Loop through the neighbors of the current node
                if neighbor not in visited:  # If the neighbor hasn't been visited
                    heapq.heappush(min_heap, (edge_weight, neighbor, current_node))  # Push the edge to the heap
    
    return total_cost  # Return the total cost of the minimum spanning tree

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open the output file

    first_multiple_input = input().rstrip().split()  # Read the first line (n and m)

    n = int(first_multiple_input[0])  # Number of nodes
    m = int(first_multiple_input[1])  # Number of edges

    edges = []  # List to store the edges

    for _ in range(m):  # Read each edge
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())  # Read the starting node

    result = prims(n, edges, start)  # Call the prims function to get the total cost

    fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file