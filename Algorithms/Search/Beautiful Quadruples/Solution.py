#!/bin/python3

import os
import sys

#
# Complete the beautifulQuadruples function below.
#
def beautifulQuadruples(a, b, c, d):
    #
    # Write your code here.
    #
    # Sort the inputs to ensure that a <= b <= c <= d
    a, b, c, d = sorted([a, b, c, d])

    # Initialize memory array to store XOR values and a counter for the total iterations
    mem = [0] * 6000
    count = 0
    total = 0

    # Iterate over values from 1 to c and d to calculate the XOR values and store their occurrences
    for i in range(1, c + 1):
        for j in range(i, d + 1):
            mem[i ^ j] += 1  # Update the memory array to track the XOR result
            total += 1  # Count the total number of pairs (i, j)

    # Iterate over values from 1 to b to compute the final count by subtracting valid pairs from total
    for i in range(1, b + 1):
        for j in range(1, min(a, i) + 1):
            count += total - mem[i ^ j]  # Subtract occurrences of XOR value from the total count
        
        for k in range(i, d + 1):
            mem[i ^ k] -= 1  # Update memory as we move through the pairs
            total -= 1  # Decrease the total count after modifying the memory

    return count  # Return the final count of beautiful quadruples
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values for a, b, c, and d
    abcd = input().split()

    a = int(abcd[0])
    b = int(abcd[1])
    c = int(abcd[2])
    d = int(abcd[3])

    # Calculate the result by calling the beautifulQuadruples function
    result = beautifulQuadruples(a, b, c, d)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    fptr.close()