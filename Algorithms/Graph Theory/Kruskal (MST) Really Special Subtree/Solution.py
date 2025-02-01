#!/bin/python3

import math  # Importing the math module for mathematical operations (though not used here)
import os  # Importing the os module for interacting with the operating system
import random  # Importing random module (though not used here)
import re  # Importing re module for regular expressions (though not used here)
import sys  # Importing sys module for system-specific parameters and functions

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts a WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, the details:
#
# 1. The number of nodes is g_nodes.
# 2. The number of edges is g_edges.
# 3. An edge exists between g_from[i] and g_to[i]. The weight of the edge is g_weight[i].
#

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Create a list of edges with their weights, and nodes they connect
    edges = list(zip(g_weight, g_from, g_to))

    # Sort edges by weight, and if weights are equal, by the nodes they connect
    edges.sort(key=lambda x: (x[0], x[1] + x[2]))

    # Union-Find (Disjoint Set Union) structure to help with cycle detection
    parent = list(range(g_nodes + 1))  # Parent list, initially each node is its own parent
    rank = [0] * (g_nodes + 1)  # Rank list for union by rank optimization

    # Find function to return the root parent of a node with path compression
    def find(node):
        if parent[node] != node:  # If the node is not its own parent
            parent[node] = find(parent[node])  # Path compression
        return parent[node]

    # Union function to merge two sets
    def union(node1, node2):
        root1 = find(node1)  # Find the root of node1
        root2 = find(node2)  # Find the root of node2

        # If the nodes are in different sets, union them
        if root1 != root2:
            if rank[root1] > rank[root2]:  # Union by rank
                parent[root2] = root1  # Make root1 the parent of root2
            elif rank[root1] < rank[root2]:  # Union by rank
                parent[root1] = root2  # Make root2 the parent of root1
            else:  # If ranks are equal, arbitrarily choose root1 and increment its rank
                parent[root2] = root1
                rank[root1] += 1
            return True  # Union was successful
        return False  # No union if both nodes are in the same set

    # Kruskal's Algorithm to find the Minimum Spanning Tree (MST)
    total_weight = 0  # Total weight of the MST
    mst_edges = 0  # Number of edges in the MST

    for weight, u, v in edges:
        if union(u, v):  # If the edge doesn't form a cycle
            total_weight += weight  # Add the edge's weight to the total weight
            mst_edges += 1  # Increment the number of edges in the MST
            if mst_edges == g_nodes - 1:  # If we've added n-1 edges, the MST is complete
                break

    return total_weight  # Return the total weight of the MST

if __name__ == '__main__':
    # Open the output file
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of nodes and edges
    g_nodes, g_edges = map(int, input().rstrip().split())

    # Initialize lists for edges
    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    # Read the edges and their weights
    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    # Call Kruskal's algorithm to get the MST weight
    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write the result to the output file
    fptr.write(str(res) + '\n')

    # Close the output file
    fptr.close()