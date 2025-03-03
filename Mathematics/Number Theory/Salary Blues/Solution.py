#!/bin/python3

import os
import sys
import math 
import functools 
from functools import reduce 

# Complete the solve function below.
def solve(a, queries):
    sol = [] 
    b = [] 

    # Compute the difference array
    for i in range(1, len(a)):
        b.append(a[i] - a[i - 1])
    
    # Compute GCD of the difference array (excluding first element)
    gc = reduce(math.gcd, b[1:]) 
    
    # Process queries
    for q in queries:
        tmp = math.gcd(a[0] + q, gc)
        sol.append(tmp) 

    return sol 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()
    n = int(nq[0])
    q = int(nq[1])

    a = list(map(int, input().rstrip().split()))
    queries = [int(input()) for _ in range(q)]

    result = solve(a, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()