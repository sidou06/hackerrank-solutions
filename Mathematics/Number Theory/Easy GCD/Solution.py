#!/bin/python3

import math  # Importing math module for mathematical operations
import os  # Importing os module for environment operations
import random  # Importing random module (not used in this code)
import re  # Importing re module for regular expressions (not used in this code)
import sys  # Importing sys module for system-specific parameters
import itertools  # Importing itertools module for combinatorial operations
from itertools import product  # Importing product function from itertools

# Function to compute all prime factors of a given number x
def all_factors(x):
    res = []  # List to store factors
    while x % 2 == 0:  # Checking divisibility by 2
        res.append(2)  # Appending 2 to the list of factors
        x //= 2  # Dividing x by 2
    for i in range(3, int(math.sqrt(x)) + 1, 2):  # Checking odd numbers up to sqrt(x)
        while x % i == 0:  # Checking divisibility by i
            res.append(i)  # Appending i to the list of factors
            x //= i  # Dividing x by i
    if x > 1:  # If x is still greater than 1, it is a prime factor
        res.append(x)  # Appending the remaining prime factor
    return res  # Returning the list of factors
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()  # Reading first line of input

    n = int(first_multiple_input[0])  # Extracting value of n
    k = int(first_multiple_input[1])  # Extracting value of k

    A = list(map(int, input().rstrip().split()))  # Reading list of integers A
    g = A[0]  # Initializing gcd with first element of A
    for i in range(1, n):  # Iterating over remaining elements
        g = math.gcd(g, A[i])  # Computing gcd of the list
    all_f = all_factors(g)  # Getting all prime factors of gcd
    r = []  # List to store modified values
    for combination in product(all_f):  # Generating combinations of factors
        m = 1  # Initializing product variable
        for num in combination:  # Iterating over factor combination
            m *= num  # Multiplying factors
        r.append(m)  # Appending product to result list
    for i in range(len(r)):  # Iterating over r list
        r[i] = k - (k % r[i])  # Adjusting values based on k
    print(max(r))  # Printing the maximum value in r