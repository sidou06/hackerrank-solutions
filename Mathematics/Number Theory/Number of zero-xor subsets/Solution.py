#!/bin/python3

import math  # Importing math module for mathematical operations
import os  # Importing os module for interacting with the operating system
import random  # Importing random module (not used in this script)
import re  # Importing re module for regular expressions (not used in this script)
import sys  # Importing sys module for system-specific functions

# Define the modulo constant (large prime number for modular arithmetic)
m = 10 ** 9 + 7

def solve(n):
    # Compute power using modular arithmetic
    # pow(base, exp, mod) computes (base^exp) % mod efficiently
    
    p = pow(2, n, m - 1)  # Compute 2^n % (m-1) using modular exponentiation
    p -= n  # Subtract n from the computed value
    p %= m - 1  # Ensure p remains within modulo (m-1)
    
    return pow(2, p, m)  # Compute 2^p % m and return the result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file for writing

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):  # Loop through each test case
        n = int(input().strip())  # Read integer n

        result = solve(n)  # Compute the result using solve function

        fptr.write(str(result) + '\n')  # Write result to output file

    fptr.close()  # Close the output file