#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # Write your code here
    A.sort()  # Sort array A in ascending order
    B.sort()  # Sort array B in ascending order
    B.reverse()  # Reverse array B to get it in descending order
    C = [x + y for x, y in zip(A, B)]  # Create a new list C with element-wise sum of A and B
    if min(C) >= k:  # If the minimum value in C is greater than or equal to k
        return "YES"  # Return "YES" if the condition is met
    else:
        return "NO"  # Return "NO" otherwise

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())  # Read the number of queries

    for q_itr in range(q):  # Process each query
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])  # Read the number of elements in the arrays
        k = int(first_multiple_input[1])  # Read the value of k

        A = list(map(int, input().rstrip().split()))  # Read array A
        B = list(map(int, input().rstrip().split()))  # Read array B

        result = twoArrays(k, A, B)  # Call the function to get the result

        fptr.write(result + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file