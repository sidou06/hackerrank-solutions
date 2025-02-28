#!/bin/python3

import math
import os
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY operations
#

def solve(n, operations):
    total = 0  # Initialize total sum
    for operation in operations:
        total += operation[2] * (operation[1] - operation[0] + 1)  # Add contribution of each operation
    return int(total / n)  # Compute the average value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])  # Read n

    m = int(first_multiple_input[1])  # Read m

    operations = []

    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))  # Read operations

    result = solve(n, operations)  # Compute result

    fptr.write(str(result) + '\n')  # Write output

    fptr.close()