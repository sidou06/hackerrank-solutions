#!/bin/python3

import math  # Importing math module for mathematical operations
import os  # Importing os module for environment operations
import random  # Importing random module (not used in this code)
import re  # Importing re module for regular expressions (not used in this code)
import sys  # Importing sys module for system-specific parameters

# List of prime numbers used for factorization
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Function to compute binomial coefficient C(n, k)
def binomial_coeff(n, k):
    if n < k:  # If n is less than k, return 0 (invalid case)
        return 0
    s = 1  # Variable to store the result
    j = k  # Assigning k to j
    if j > n - k:  # Choosing the smaller value for efficiency
        j = n - k
    for i in range(1, j + 1):  # Loop to compute binomial coefficient
        s = (s * (n - (i - 1))) / i  # Using multiplicative formula
    return s  # Returning the computed coefficient

# Function to compute the remainder using Lucas' theorem
def lucas_remainder(n, k, m):
    s = 1  # Variable to store the result
    kp = k  # Copy of k
    np = n  # Copy of n
    mp = m  # Copy of m
    while kp > 0:  # Process digits in base m
        tmp_n = np % mp  # Extracting last digit of n in base m
        tmp_k = kp % mp  # Extracting last digit of k in base m
        s = (s * (binomial_coeff(tmp_n, tmp_k) % mp)) % mp  # Computing remainder
        kp //= mp  # Reducing k
        np //= mp  # Reducing n
    return s  # Returning the computed remainder
            
# Function to compute the solution using Lucas' theorem and Chinese Remainder Theorem
def solve(n, r, m):
    ans = -1  # Initial answer
    last = 1  # Variable to store product of prime factors
    if m == 1:  # Special case when m is 1
        return 0
    i = 0  # Index for prime numbers list
    while (i < len(primes) and m > 1):  # Loop through primes while m is greater than 1
        if (m % primes[i] == 0):  # If m is divisible by the prime
            rem = lucas_remainder(n, r, primes[i])  # Compute remainder using Lucas' theorem
            if ans == -1:  # If ans is not set, initialize it
                ans = rem 
            else:
                for j in range(50):  # Loop to solve for ans using Chinese Remainder Theorem
                    if ((ans + (last * j)) % primes[i] == rem):  # Checking for valid value
                        ans += last * j  # Updating answer
                        break 
            last *= primes[i]  # Updating last to include current prime factor
            m /= primes[i]  # Reducing m by dividing it with the prime factor
        i += 1  # Moving to the next prime
    return int(ans)  # Returning the computed result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Opening output file for writing

    t = int(input().strip())  # Reading number of test cases

    for t_itr in range(t):  # Iterating over test cases
        first_multiple_input = input().rstrip().split()  # Reading input values

        n = int(first_multiple_input[0])  # Extracting n
        r = int(first_multiple_input[1])  # Extracting r
        m = int(first_multiple_input[2])  # Extracting m

        result = solve(n, r, m)  # Computing result using solve function

        fptr.write(str(result) + '\n')  # Writing result to output file

    fptr.close()  # Closing output file