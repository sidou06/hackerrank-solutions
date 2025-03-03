#!/bin/python3

import math  # Importing math module for mathematical operations
import os  # Importing os module for file handling
import random  # Importing random module (not used in this code)
import re  # Importing re module for regular expressions (not used in this code)
import sys  # Importing sys module for system-specific parameters

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def solve(n):
    # Function to compute the total number of divisors of n factorial
    factors = {}  # Dictionary to store prime factors and their exponents
    sieve = [True] * (n + 1)  # Boolean array for Sieve of Eratosthenes
    
    for p in range(2, n + 1):  # Iterate over numbers from 2 to n
        if sieve[p]:  # If p is a prime number
            exponent = 0  # Initialize exponent count
            power = p  # Start with the prime number
            
            # Compute exponent of prime p in n!
            while power <= n:
                exponent += n // power  # Count multiples of power in n!
                power *= p  # Increase power
            
            factors[p] = 2 * exponent + 1  # Compute factor count for p
            
            # Mark multiples of p as not prime
            for m in range(p * p, n + 1, p):
                sieve[m] = False  
    
    tot = 1  # Initialize total product of factors
    mod = 10 ** 6 + 7  # Modulo value for large numbers
    
    for expo in factors.values():  # Iterate over computed exponents
        tot *= expo  # Multiply factor counts
        tot %= mod  # Apply modulo to avoid overflow
    
    return tot  # Return final computed value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open file for writing output

    n = int(input().strip())  # Read input integer

    result = solve(n)  # Compute result

    fptr.write(str(result) + '\n')  # Write result to file

    fptr.close()  # Close file