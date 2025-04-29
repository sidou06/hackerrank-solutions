#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(a):
    p = 1  # Initialize product to 1
    m = 10 ** 9 + 7  # Define modulus to prevent overflow and meet problem constraints

    for ele in a:
        # For each element, compute (2^ele + 1) % m and multiply to the running product
        p *= ((pow(2, ele, m) + 1) % m)
        p %= m  # Apply modulus at each step to keep p within limits

    return p - 1  # Subtract 1 from final product to get the result (as per problem definition)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file defined by the system

    a_count = int(input())  # Read number of elements in array

    a = list(map(int, input().rstrip().split()))  # Read array elements

    result = solve(a)  # Compute result using solve function

    fptr.write(str(result) + '\n')  # Write result to output file

    fptr.close()  # Close output file