#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anotherMinimaxProblem' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def anotherMinimaxProblem(a):
    # If all elements in the array are 0, return 0
    if all(x == 0 for x in a): 
        return 0

    n = len(a)
    max_bit = max(a).bit_length()  # Get the bit length of the largest number

    # Iterate through each bit from most significant to least significant
    for bit in range(max_bit - 1, -1, -1):
        ones, zeros = [], []
        for num in a:
            if num & (1 << bit):  # If the bit is set
                ones.append(num)
            else:  # If the bit is not set
                zeros.append(num)
        # If there are numbers in both ones and zeros, break the loop
        if zeros and ones:
            break

    # If no numbers with different bits are found, return the minimum XOR of any two numbers
    if not zeros or not ones:
        return min(a[i] ^ a[j] for i in range(n) for j in range(i + 1, n))

    # Otherwise, return the minimum XOR between numbers from the two groups (ones and zeros)
    return min(x ^ y for x in zeros for y in ones)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read the size of the array

    a = list(map(int, input().rstrip().split()))  # Read the array of integers

    result = anotherMinimaxProblem(a)  # Compute the result

    fptr.write(str(result) + '\n')  # Write the result to output

    fptr.close()