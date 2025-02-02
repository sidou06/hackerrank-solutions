#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right

#
# Complete the 'redJohn' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

# Function to check if a number is prime
def is_prime(x):
    for j in range(2,int(math.sqrt(x)) + 1):
        if x % j == 0:
            return False
    return True

# List of prime numbers up to 10^6
primes = [x for x in range(2,10 ** 6) if is_prime(x)]

# Function to calculate combination (n choose k)
def comb(n,k):
    if k < n - k:
        k = n - k
    nom = 1
    denom = 1
    # Calculate the numerator
    for i in range(k + 1,n + 1):
        nom *= i
    # Calculate the denominator
    for i in range(2,n - k + 1):
        denom *= i
    return nom // denom

# Function to calculate the redJohn problem solution
def redJohn(n):
    # Calculate the number of cases (n // 4)
    cases = n // 4
    total = 1
    # Sum combinations for each case
    for quads in range(1,cases + 1):
        total += comb(quads + n - quads * 4, quads)
    
    # Return the index of the total value in the prime list
    return bisect_right(primes,total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Input number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        # Input value for n
        n = int(input().strip())

        # Get result of redJohn function
        result = redJohn(n)

        # Write the result to the output
        fptr.write(str(result) + '\n')

    fptr.close()