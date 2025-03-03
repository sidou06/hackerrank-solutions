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
# The function accepts INTEGER n as parameter.
#

def sum_digits(a):
    # Recursively sum the digits of a number
    if a < 10:
        return a  # Base case: single-digit number
    else:
        return a % 10 + sum_digits(a // 10)  # Extract last digit and recurse on remaining digits
        
def factors(N):
    # Compute the prime factorization of N
    C = N 
    factors = []  # List to store prime factors
    primes = []  # List to store discovered primes
    i = 2
    repeat = False 
    while i < int(math.sqrt(C)) + 1:
        p = True 
        j = 0 
        while j < len(primes) and p and not repeat:
            if i % primes[j] == 0:
                p = False  # i is not prime if divisible by any known prime
            j += 1 
        if p:
            if not repeat:
                primes.append(i)  # Store i as a prime number
            if C % i == 0:
                factors.append(i)  # Add prime factor to the list
                C //= i  # Reduce C by dividing by i
                i -= 1  # Stay at the same value to check for repeated factors
                repeat = True
            else:
                repeat = False 
        i += 1
    if C != 1: 
        factors.append(int(C))  # Add any remaining prime factor
    return factors 
            
                
def solve(n):
    # Check if the number is a Smith number
    fac = factors(n)  # Get prime factors of n
    s = sum_digits(n)  # Compute sum of digits of n
    d = 0 
    for f in fac:
        d += sum_digits(f)  # Compute sum of digits of all prime factors
    if d == s:
        return 1  # Smith number
    else:
        return 0  # Not a Smith number

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read input number

    result = solve(n)  # Determine if it's a Smith number

    fptr.write(str(result) + '\n')

    fptr.close()