#!/bin/python3

import math
import os
import random
import re
import sys

cum_weight = dict()  # Dictionary to store cumulative weights for each node
child_parent = dict()  # Dictionary to store the parent of each node

min_t = [float('inf')]  # Variable to keep track of the minimum difference in weights

def dfs_iterative(G, s, weights):
    # Calculate the total weight of all nodes
    total = sum(weights)

    stack = [s]  # Stack for DFS traversal, starting from the root node (s)
    visited = set()  # Set to track visited nodes

    while stack:
        vertex = stack[-1]  # Get the current vertex from the top of the stack
        if vertex in visited:
            # Logic to calculate the cumulative weight for the current node
            cum_weight[vertex] = weights[vertex - 1]  # Initialize with the node's weight
            for c in G[vertex]:  # Iterate over the children of the node
                if child_parent.get(c, -1) == vertex:
                    cum_weight[vertex] += cum_weight[c]  # Add the cumulative weight of the child
            
            # Calculate the difference between total weight and twice the cumulative weight
            min_t[0] = min(
                min_t[0],
                abs(total - 2 * cum_weight[vertex])  # Find the minimum difference
            )
            stack.pop()  # Pop the current vertex from the stack
            continue
        visited.add(vertex)  # Mark the current vertex as visited
        for neighbor in G[vertex]:  # Iterate over the neighbors of the current vertex
            if neighbor not in visited:
                child_parent[neighbor] = vertex  # Set the current vertex as the parent of the neighbor
                stack.append(neighbor)  # Push the neighbor to the stack for further exploration
    
    return visited

def setGraph(nCount, edges):
    """
    Boilerplate method to set the graph
    :param nCount: Number of nodes in the graph
    :param edges: List of edges in the graph
    :return: Graph represented as an adjacency list
    """
    g = dict()  # Dictionary to store the graph

    # Set the nodes and their edges
    for _t, _e in edges:
        if _t not in g.keys():
            g[_t] = [_e]  # Create an adjacency list for the node
        else:
            g[_t].append(_e)
        if _e not in g.keys():
            g[_e] = [_t]  # Create an adjacency list for the other node in the edge
        else:
            g[_e].append(_t)
    
    # Add zombie nodes (nodes with no edges)
    g.update({k: [] for k in range(1, nCount + 1) if k not in g.keys()})
    
    return g

def cutTheTree(nodes, edges):
    # Create the graph from the nodes and edges
    G = setGraph(len(nodes), edges)
    print(G)  # Print the graph for debugging
    dfs_iterative(G, 1, nodes)  # Perform DFS starting from node 1 (root node)
    return min_t[0]  # Return the minimum difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read the number of nodes

    data = list(map(int, input().rstrip().split()))  # Read the weight of each node

    edges = []  # List to store the edges

    # Read the edges between nodes
    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    # Calculate the result and write it to the output
    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()