#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#

import heapq

def getCost(g_nodes, g_from, g_to, g_weight):
    graph = {node : set() for node in range(1,g_nodes + 1)}  # Initialize graph with empty sets for each node
    for i in range(len(g_from)):  # Loop through each edge
        graph[g_from[i]].add((g_to[i], g_weight[i]))  # Add edges in both directions with weights
        graph[g_to[i]].add((g_from[i], g_weight[i]))  
        
    cost = {node : float('inf') for node in range(1,g_nodes + 1)}  # Initialize cost to infinity for all nodes
    cost[1] = 0  # Set the starting node's cost to 0
    pq = [(0 , 1)]  # Initialize priority queue with the starting node
    
    while pq:  # While there are nodes to process
        current_cost, current_station = heapq.heappop(pq)  # Get the node with the minimum cost
        if current_station == g_nodes:  # If we've reached the target node
            return current_cost  # Return the total cost
        
        if current_cost > cost[current_station]:  # If this path is not optimal, skip it
            continue
        
        for neighbor, next_cost in graph[current_station]:  # Loop through neighbors of the current node
            tmp =  max(0, next_cost - current_cost)  # Calculate the cost difference
            total = current_cost + tmp  # Add the cost to the total path cost
            if total < cost[neighbor]:  # If this path offers a lower cost to the neighbor
                cost[neighbor] = total  # Update the cost for the neighbor
                heapq.heappush(pq, (total, neighbor))  # Push the neighbor to the priority queue
    
    return "NO PATH EXISTS"  # If no path to the target exists
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file

    g_nodes, g_edges = map(int, input().rstrip().split())  # Read number of nodes and edges

    g_from = [0] * g_edges  # Initialize list for 'from' nodes
    g_to = [0] * g_edges  # Initialize list for 'to' nodes
    g_weight = [0] * g_edges  # Initialize list for edge weights

    for i in range(g_edges):  # Read each edge
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    result = getCost(g_nodes, g_from, g_to, g_weight)  # Get the minimum cost
    fptr.write(str(result) + '\n')  # Write result to output file
    fptr.close()  # Close the output file