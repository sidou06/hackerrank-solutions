#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Calculate the total number of balls in each container and the total number of each type of ball
    n = len(container)
    cont = [0] * n
    typ = [0] * n
    for i in range(n):
        for j in range(n):
            cont[i] += container[i][j]
            typ[j] += container[i][j]

    # If the sorted list of containers' ball counts matches the sorted list of ball types' counts, it's possible to organize
    if sorted(cont) == sorted(typ):
        return "Possible"
    return "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())  # Read the number of test cases

    for q_itr in range(q):
        n = int(input().strip())  # Read the size of the container matrix

        container = []  # Initialize the container matrix

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)  # Call the function

        fptr.write(result + '\n')  # Write the result for the current test case

    fptr.close()