#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

from math import sqrt

primes = []  # List to store prime numbers

def is_prime(n):
    # Function to check if a number is prime
    i = 0
    sq = int(math.sqrt(n)) + 1
    while i < len(primes):
        if primes[i] > sq:
            return True 
        elif (n % primes[i] == 0):
            return False
        i += 1
    return True 

# Generate prime numbers up to sqrt(10^9)
for i in range(3, int(math.sqrt(10 ** 9)) + 1, 2):
    if is_prime(i):
        primes.append(i) 

def solve(n, m):
    # Initialize count of twin primes
    total = 0  
    
    # Ensure n starts from at least 3
    n = max(3, n)  
    
    # If n is even, move to the next odd number
    if n % 2 == 0:
        n = n + 1
    
    # Handle small cases for n
    if n <= 3:
        if m > 6:
            total += 2 
        elif m > 4:
            total += 1
        n = 11  
    elif n <= 5 and m > 6:
        total += 1
        n = 11  
    
    # Determine the starting point in a 30-number cycle
    b = n % 30  
    if b <= 11:
        it = 0  
        n = ((n // 30) * 30) + 11  
    elif b <= 17: 
        it = 1  
        n = ((n // 30) * 30) + 17  
    else:
        it = 2  
        n = ((n // 30) * 30) + 29  
    
    # Loop through numbers checking for twin primes
    while (n + 2 <= m):  
        if it == 0:
            if is_prime(n) and is_prime(n + 2):
                total += 1  
            n += 6  
        else:
            if is_prime(n) and is_prime(n + 2):
                total += 1
            n += 12  
        it = (it + 1) % 3  
    
    return total  # Return total count of twin primes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])  # Read integer n
    m = int(first_multiple_input[1])  # Read integer m

    result = solve(n, m)  # Calculate number of twin primes in range

    fptr.write(str(result) + '\n')

    fptr.close()