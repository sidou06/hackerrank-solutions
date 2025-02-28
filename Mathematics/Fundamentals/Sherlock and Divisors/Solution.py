#!/bin/python3

import math
import os
import sys

#
# Complete the 'divisors' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def divisors(n):
    nb = 0  # Initialize the count of divisors
    while n % 2 == 0:  # Count the power of 2 in the prime factorization
        nb += 1
        n //= 2 
    for i in range(3, int(n ** 0.5) + 1, 2):  # Iterate through odd numbers
        cpt = 1  # Initialize count for current prime factor
        while n % i == 0:  # Count occurrences of prime factor i
            cpt += 1 
            n //= i 
        nb *= cpt  # Multiply count of divisors
    if n > 2:  # If n is still greater than 2, it's a prime factor
        nb *= 2
    return nb 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        n = int(input().strip())  # Read input value

        result = divisors(n)

        fptr.write(str(result) + '\n')  # Write output

    fptr.close()