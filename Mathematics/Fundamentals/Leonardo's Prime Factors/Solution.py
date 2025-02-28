#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def is_prime(n):
    # Check if the number is less than 2 (not prime)
    if n < 2:
        return False
    else:
        # Check divisibility from 2 to sqrt(n)
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

# Precompute the primes whose product is <= 10^18
Primes = []
i = 2  # Start from the smallest prime
prod = 1  # Initialize product of primes
while prod <= 10**18:
    if is_prime(i):  # Check if i is prime
        Primes.append(i)  # Store the prime number
        prod = prod * i  # Multiply to get cumulative product
    i = i + 1  # Move to the next number

def primeCount(n):
    # Initialize count and product
    count = 0
    product = 1
    # Multiply primes until the product exceeds n
    while (product <= n):
        product = product * Primes[count]
        count = count + 1
    return count - 1  # Subtract 1 because last product exceeded n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of test cases
    q = int(input().strip())

    for q_itr in range(q):
        # Read input value for each test case
        n = int(input().strip())

        # Compute the result using the function
        result = primeCount(n)

        # Write the result to output
        fptr.write(str(result) + '\n')

    fptr.close()