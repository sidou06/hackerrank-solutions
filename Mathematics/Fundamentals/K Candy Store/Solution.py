#!/bin/python3

import math
import os
import random
import re
import sys

# Modulo value to prevent overflow
m = 10 ** 9 

# Precompute table T to store computed values
T = []
for i in range(1000):
    T.append([1])  # Initialize first column with 1

# Fill the first row with consecutive values
for i in range(999):
    T[0].append(i + 2) 

# Compute the table using dynamic programming
for i in range(1, 1000):
    for j in range(1, 1000):
        # Fill the table using the sum of previous values mod m
        T[i].append((T[i][j - 1] + T[i - 1][j]) % m)

# Function to return the precomputed value for given (n, k)
def solve(n, k):
    return T[k - 1][n - 1]  # Return the computed value from table T

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        n = int(input().strip())  # Read n
        k = int(input().strip())  # Read k

        result = solve(n, k)  # Get result from precomputed table

        fptr.write(str(result) + "\n")  # Write output to file
    
    fptr.close()