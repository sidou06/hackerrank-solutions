#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

def initialize(s):
    # This function is called once before all queries.
    alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
    start = [0] * 26  # Initialize the start array with 26 zeros
    current = [0] * 26  # Initialize the current array with 26 zeros
    states = [start]  # Initialize states with the starting state
    for l in s:  # Iterate through the string
        current[alphabet[l]] += 1  # Update the count for the current character
        now = current.copy()  # Create a copy of the current state
        states.append(now)  # Add the new state to the states list
    return states

#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

mod = 10 ** 9 + 7

def fact_mod(a):
    res = [1, 1]  # Initialize factorial array with the first two values
    for i in range(2, a + 1):  # Calculate factorials modulo mod
        t = res[-1] * i
        res.append(t % mod)
    return res

def calcul_denom(denom, facts):
    res = 1
    for elem in denom:  # Calculate the denominator
        x = facts[elem]
        res *= x 
        res %= mod
    return res

def answerQuery(l, r, states, facts):
    nom = 0
    denom = []
    impairs = 0
    for i in range(26):  # Iterate over the 26 letters of the alphabet
        x = states[r][i] - states[l - 1][i]  # Get the difference in counts of characters
        nom += x // 2  # Add half of the even occurrences to the numerator
        if x > 3:  # If more than 3 occurrences, add it to the denominator list
            denom.append(x // 2)
        impairs += x % 2  # Count the odd occurrences
    nom = facts[nom]  # Get the factorial of the numerator
    denom = calcul_denom(denom, facts)  # Calculate the denominator
    denom = pow(denom, mod - 2, mod)  # Compute the modular inverse of the denominator
    result = (nom * denom) % mod  # Final result is numerator * inverse of denominator
    if impairs:
        result *= impairs  # If there are odd occurrences, multiply the result by impairs
        result %= mod  # Take the result modulo mod
    return result  # Return the result for this query modulo 1000000007.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    states = initialize(s)  # Initialize the states with the given string
    facts = fact_mod(len(states) // 2)  # Calculate factorials for all necessary values
    q = int(input().strip())  # Read the number of queries

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r, states, facts)

        fptr.write(str(result) + '\n')

    fptr.close()