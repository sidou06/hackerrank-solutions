#!/bin/python3

import os
import sys

#
# Complete the 'isFibo' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

Fibo = [0,1]  # Initialize Fibonacci sequence
i = 1
while Fibo[i] <= 10**10:
    Fibo.append(Fibo[i] + Fibo[i - 1])  # Generate Fibonacci numbers
    i = i + 1

def isFibo(n):
    res = 'IsNotFibo'  # Default result
    k = 0
    while res == 'IsNotFibo' and Fibo[k] <= n:
        if Fibo[k] == n:
            return 'IsFibo'  # Found in Fibonacci sequence
        k = k + 1
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        n = int(input().strip())  # Read input number

        result = isFibo(n)  # Check if Fibonacci

        fptr.write(result + '\n')  # Write output

    fptr.close()