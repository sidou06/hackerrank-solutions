#!/bin/python3

import math
import os
import random
import re
import sys

# Function to calculate the sum of digits of a number
def sum_digits(x):
    return sum(int(digit) for digit in str(x))

# Function to find all divisors of a number
def divisors(x):
    RES = []
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            RES.append(i)
    return RES

if __name__ == '__main__':
    n = int(input().strip())
    
    best = n
    Div = divisors(n)

    # Find the divisor with the highest sum of digits
    for j in range(len(Div), 0, -1):
        if sum_digits(Div[j - 1]) >= sum_digits(best):
            best = Div[j - 1]

    print(best)