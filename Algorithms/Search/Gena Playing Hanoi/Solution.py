#!/bin/python3

import math
import os
import random
import re
import sys
import collections

def minMoves(arr, n):
    # Number of rods (fixed to 4 rods for the Tower of Hanoi problem)
    N = 4

    # Goal is to have all discs on the last rod (represented by setting all bits to 1)
    goal = 2**n - 1

    # Initialize rods as a list of zeros (no discs are on any rod initially)
    rods = [0 for _ in range(N)]
    for i in range(len(arr)-1,-1,-1):
        # Place the discs on the corresponding rods (setting the corresponding bits)
        rods[arr[i]-1] = rods[arr[i]-1] | 1 << i

    # If the first rod already has all discs, no moves are needed
    if rods[0] == goal:  
        return 0

    # Helper functions for manipulating the bits representing discs on rods:
    def add_disc(rod, i): return rod | 1 << i  # Add a disc by setting the ith bit to 1
    def pop_disc(rod, i): return rod & ~(1 << i)  # Remove a disc by setting the ith bit to 0
    def top_disc(rod):
        i = 0
        while rod & 1 != 1:  # Find the rightmost set bit (the top disc)
            rod >>= 1
            i += 1
        return i

    # Convert the rods to a tuple to make it hashable for the visited set
    rods = tuple(rods)

    # BFS setup: queue for BFS with the initial state and number of moves
    bfs = collections.deque([ (rods, 0) ])
    visited = set([ rods ])  # Set of visited states to avoid revisiting the same state

    while bfs:
        rods, moves = bfs.popleft()  # Get the current state of rods and the move count
        for i in range(N):
            if rods[i] != 0:  # If the current rod is not empty
                d1 = top_disc(rods[i])  # Get the top disc from the current rod
                for j in range(N):
                    # Get the top disc of the destination rod if it's not empty, else -1
                    d2 = top_disc(rods[j]) if rods[j] != 0 else -1
                    # Check if we can move the disc to the destination rod (either it's empty or the top disc is smaller)
                    if rods[j] == 0 or d1 < d2:
                        new_rods = list(rods)  # Create a copy of the rods list
                        # Move the top disc from rod i to rod j
                        new_rods[i] = pop_disc(new_rods[i], d1)
                        new_rods[j] = add_disc(new_rods[j], d1)
                        # Sort rods 1, 2, and 3 to ensure the discs are in the correct order
                        new_rods[1:4] = sorted(new_rods[1:4])
                        new_rods = tuple(new_rods)  # Convert back to a tuple

                        # If the new configuration hasn't been visited
                        if new_rods not in visited:
                            # If the goal is reached (all discs on the first rod)
                            if new_rods[0] == goal:
                                return moves + 1
                            # Otherwise, mark the new configuration as visited and add to the queue
                            visited.add(new_rods)
                            bfs.append((new_rods, moves + 1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read the number of discs

    loc = list(map(int, input().rstrip().split()))  # Read the initial positions of the discs

    res = minMoves(loc, len(loc))  # Get the minimum number of moves to solve the problem

    fptr.write(str(res) + '\n')  # Write the result to the output file

    fptr.close()