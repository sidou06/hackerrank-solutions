#!/bin/python3

import math  # Importing math module for mathematical operations (though not used here)
import os  # Importing os module to interact with the operating system
import random  # Importing random module for generating random numbers (though not used here)
import re  # Importing re module for regular expressions (though not used here)
import sys  # Importing sys module for system-specific parameters and functions
from collections import defaultdict  # Importing defaultdict from collections module (though not used here)
from collections import deque  # Importing deque from collections for fast queue operations

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n - number of nodes
#  2. INTEGER m - number of edges
#  3. 2D_INTEGER_ARRAY edges - list of edges (each pair of nodes connected by an edge)
#  4. INTEGER s - starting node for BFS

def bfs(n, m, edges, s):
    # Initialize the graph as an empty dictionary of sets (each set holds the neighbors of a node)
    graph = {node: set() for node in range(1, n + 1)}

    # Populate the graph with the given edges
    for edge in edges:
        graph[edge[0]].add(edge[1])  # Add an edge from node[0] to node[1]
        graph[edge[1]].add(edge[0])  # Add an edge from node[1] to node[0] (undirected graph)

    # Print the graph (for debugging purposes)
    print(graph)

    # Initialize the depth dictionary to store the distance of each node from the start node 's'
    # Initially set all node distances to -1 (unvisited)
    depth = {node: -1 for node in range(1, n + 1)}
    depth[s] = 0  # The starting node's depth is 0

    # Create a queue (using deque for efficient pop from the left) for BFS
    queue = deque([s])  # Start with the node 's' in the queue

    # Perform BFS
    while queue:
        node = queue.popleft()  # Dequeue the next node to explore
        for neighbor in graph[node]:  # Loop through each neighbor of the current node
            if depth[neighbor] == -1:  # If the neighbor has not been visited
                depth[neighbor] = depth[node] + 6  # Set the neighbor's distance to current node's distance + 6
                queue.append(neighbor)  # Enqueue the neighbor for further exploration

    # Collect all the distances except for the starting node (which is 0) and return them
    res = [depth[node] for node in depth if depth[node] != 0]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open the output file

    q = int(input().strip())  # Read the number of test cases

    # Loop through each test case
    for q_itr in range(q):
        # Read the number of nodes (n) and the number of edges (m)
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])  # Number of nodes
        m = int(first_multiple_input[1])  # Number of edges

        edges = []  # List to store the edges between nodes
        # Read the edges
        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))  # Read each edge and append to the list

        s = int(input().strip())  # Read the starting node for BFS

        # Call the bfs function to get the shortest paths from the start node
        result = bfs(n, m, edges, s)

        # Write the result to the output file (space-separated values)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()  # Close the output file