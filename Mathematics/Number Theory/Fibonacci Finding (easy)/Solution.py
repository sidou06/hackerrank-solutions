#!/bin/python3

import math
from math import sqrt as sq 
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER n
#

# Function to compute the square of a transformation matrix
def matrix_sqr(a):
    d = a[0]
    e = a[1]
    c = (d * d) % modul + (e * e) % modul 
    h = (d * e) % modul + (e * (d - e)) % modul
    return [c % modul, h % modul]
    
# Function to multiply two transformation matrices
def mat_mul(e, f):
    a = e[0]
    b = e[1]
    c = f[0]
    d = f[1]
    return [((a * c) % modul + (b * d) % modul) % modul, ((a * d) % modul + (b * (c - d)) % modul) % modul]
    
modul = 10 ** 9 + 7  # Modulo value to prevent overflow

def solve(a, b, n):
    j = 0
    m = [[1,1]]  # Initial transformation matrix
    
    # Base case
    if n == 1:
        return b  
    
    # Finding the largest power of 2 <= (n-1)
    while 2 ** j <= n - 1:
        j += 1
    j -= 1  # Adjust index
    
    # Compute transformation matrices using exponentiation by squaring
    for i in range(j):
        m.append(matrix_sqr(m[i]))
    
    cu = m[j]  # Start with the highest power
    n -= 2 ** j  
    j -= 1  
    
    # Multiply matrices to reach exact exponent
    while n - 1 > 0:
        if 2 ** j <= n - 1:
            cu = mat_mul(cu, m[j])
            n -= 2 ** j  
        j -= 1  
    
    # Compute final answer using transformation matrix
    ans = ((b * cu[0]) % modul + (a * cu[1]) % modul) % modul 
    return ans 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])  # Read a
        b = int(first_multiple_input[1])  # Read b
        n = int(first_multiple_input[2])  # Read n

        result = solve(a, b, n)  # Compute result

        fptr.write(str(result) + '\n')

    fptr.close()