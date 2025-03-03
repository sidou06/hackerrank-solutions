#!/bin/python3

import math
import itertools 
import decimal 
import os
import random
import re
import sys

def factors(s):
    # Compute the prime factors of s
    arr = []
    if s % 2 == 0:
        arr.append(2)  # Add 2 to the list of factors
        s //= 2 
    while s % 2 == 0:
        s //= 2  # Remove all occurrences of 2
    for i in range(3, int(math.sqrt(s)) + 1, 2):
        if s % i == 0:
            arr.append(i)  # Add factor i
            s //= i 
        while s % i == 0:
            s //= i  # Remove all occurrences of i
        if s == 1:
            break 
    if s > 1:
        arr.append(s)  # Add remaining prime factor if any
    return arr 

if __name__ == '__main__':
    p = int(input().strip())  # Read input value
    s = p - 1  # Compute s as p - 1
    arr = factors(s)  # Get prime factors of s
    f = arr.copy()  # Copy factor list
    for i in range(len(arr)):
        arr[i] = s // arr[i]  # Compute divisors of s

    a = 2  # Start with base value
    found = False 
    while not found:
        stop = False 
        j = 0
        while not stop and j < len(arr):
            if pow(a, arr[j], p) == 1:  # Check if a^arr[j] mod p == 1
                stop = True 
            j += 1
        if not stop:
            found = True  # Found the smallest primitive root
            break 
        a += 1 
        if int(math.sqrt(a)) ** 2 == a:
            a += 1  # Skip perfect squares

    products = [] 
    for r in range(1, len(f) + 1):
        products.append([])
        for c in itertools.combinations(f, r):
            p = 1 
            for n in c:
                p *= n  # Compute product of factors
            products[r-1].append(p)

    total = s - 2  # Initialize total count
    for i in range(len(products)):
        for j in range(len(products[i])):
            if i % 2 == 0:
                total -= (s - 1) // products[i][j]  # Apply inclusion-exclusion principle
            else:
                total += (s - 1) // products[i][j]         

    """ 
    Alternative method to count numbers coprime with s:
    for i in range(3, s, 2):
        if math.gcd(s, i) == 1:
            nb += 1
    """

    print(str(a) + " " + str(total + 1))  # Output the result
    # Write your code here