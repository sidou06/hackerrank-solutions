#!/bin/python3

import math  # Import math module for mathematical operations
import os  # Import os module for file operations
import sys  # Import sys module for system-specific parameters

# Function to compute the least common multiple (LCM) of two numbers
def lcm(a, b):
    return a * b // math.gcd(a, b)  # LCM formula using greatest common divisor (GCD)

# Function to compute an array b based on array a
def solve(a):
    b = [a[0]]  # Initialize array b with the first element of a
    for i in range(len(a) - 1):  # Iterate over elements of a
        b.append(lcm(a[i], a[i + 1]))  # Append LCM of consecutive elements
    b.append(a[-1])  # Append the last element of a to b
    return b  # Return the resulting array b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file for writing

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):  # Iterate over test cases
        a_count = int(input().strip())  # Read the number of elements in array a

        a = list(map(int, input().rstrip().split()))  # Read array a

        result = solve(a)  # Compute result using solve function

        fptr.write(' '.join(map(str, result)))  # Write result to output file
        fptr.write('\n')  # Write newline character

    fptr.close()  # Close output file