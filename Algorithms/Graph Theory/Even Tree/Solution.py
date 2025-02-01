#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    tree = defaultdict(list)  # Initialize the tree using defaultdict
    for i in range(len(t_from)):  # Iterate through the edges
        tree[t_from[i]].append(t_to[i])  # Add the edge to the tree
        tree[t_to[i]].append(t_from[i])  # Add the reverse edge to the tree
    subtree_size = [0] * (t_nodes + 1)  # Initialize the array to store subtree sizes
    visited = [False] * (t_nodes + 1)  # Initialize the visited array
    removable_edges = 0  # Variable to count removable edges

    def dfs(node):  # Depth-first search to calculate subtree sizes
        nonlocal removable_edges  # Access the outer removable_edges variable
        visited[node] = True  # Mark the current node as visited
        size = 1  # Start with size 1 (the current node)
        for neighbor in tree[node]:  # Explore neighbors of the current node
            if not visited[neighbor]:  # If the neighbor hasn't been visited
                child_size = dfs(neighbor)  # Recursively calculate the child's size
                if child_size % 2 == 0:  # If the child size is even, it can be removed
                    removable_edges += 1
                else:  # Otherwise, add the child's size to the current node's size
                    size += child_size
        subtree_size[node] = size  # Store the size of the subtree rooted at the current node
        return size  # Return the size of the current subtree

    dfs(1)  # Start DFS from the root node (node 1)
    return removable_edges  # Return the count of removable edges

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open the output file

    t_nodes, t_edges = map(int, input().rstrip().split())  # Read number of nodes and edges

    t_from = [0] * t_edges  # Initialize array to store edges from nodes
    t_to = [0] * t_edges  # Initialize array to store edges to nodes

    for i in range(t_edges):  # Read the edges
        t_from[i], t_to[i] = map(int, input().rstrip().split())  # Store each edge

    res = evenForest(t_nodes, t_edges, t_from, t_to)  # Call the evenForest function

    fptr.write(str(res) + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file