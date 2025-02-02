#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

def beautifulPairs(A, B):
    # Initialize the count of beautiful pairs
    cp = 0        
    
    # Get unique elements from list B
    b = list(set(B))
    
    # Count the minimum occurrences of each element in both lists
    for i in range(len(b)): 
        ele = b[i]
        cp += min(A.count(ele), B.count(ele))
    
    # If all elements match, one must be changed, reducing the count by 1
    if cp == n:
        return n - 1

    # Otherwise, we can increase the count by changing one element
    return cp + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of elements in lists A and B
    n = int(input().strip())

    # Read list A
    A = list(map(int, input().rstrip().split()))

    # Read list B
    B = list(map(int, input().rstrip().split()))

    # Compute the result
    result = beautifulPairs(A, B)

    # Write the result to output
    fptr.write(str(result) + '\n')

    fptr.close()