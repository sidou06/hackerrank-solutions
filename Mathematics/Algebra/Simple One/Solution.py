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
#  1. INTEGER p
#  2. INTEGER q
#  3. INTEGER n
#

from fractions import Fraction

MOD = 1000000007

# Extended Euclidean Algorithm to compute the greatest common divisor and the coefficients
def egcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0

# Function to compute modular inverse of a with respect to modulus m
def modinv(a, m):
    _, x, _ = egcd(a, m)
    return x % m

# Function to compute the tangent of a fraction 'a' raised to the power of 'k' using continued fractions
def ntan(a, k):
    b = Fraction(0)
    if k == 0:
        return b
    if k == 1:
        return a
    while k != 0:
        if k % 2 == 1:
            b = (a + b) / (1 - a * b)
            b = Fraction(b.numerator % MOD, b.denominator % MOD)
        a = 2 * a / (1 - a * a)
        a = Fraction(a.numerator % MOD, a.denominator % MOD)
        k //= 2
    return b

# Main function to compute the result
def solve(p, q, n):
    # Calculate the nth tangent of p/q
    a = ntan(Fraction(p, q), n)
    # Return the result as the numerator divided by the modular inverse of the denominator
    return ((a.numerator * modinv(a.denominator, MOD)) % MOD)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of test cases
    t = int(input().strip())

    # Iterate through each test case
    for t_itr in range(t):
        # Read p, q, and n
        first_multiple_input = input().rstrip().split()
        p = int(first_multiple_input[0])
        q = int(first_multiple_input[1])
        n = int(first_multiple_input[2])

        # Get the result by solving the equation
        result = solve(p, q, n)

        # Write the result to output
        fptr.write(str(result) + '\n')

    fptr.close()