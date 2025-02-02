#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # List to store important contests' luck values
    imp = [] 
    # Variable to store total luck balance
    luck = 0 

    # Iterate through contests
    for i in range(len(contests)):
        if contests[i][1] == 0:  # If the contest is not important
            luck += contests[i][0]  # Add luck to the total balance
        else:
            imp.append(contests[i][0])  # Store important contest luck values
    
    # Sort important contests in descending order
    imp.sort()
    imp.reverse()
    
    # Add luck from the top k important contests
    luck += sum(imp[:k])
    # Subtract luck from the remaining important contests that must be won
    luck -= sum(imp[k:])
    
    return luck 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the first line of input
    first_multiple_input = input().rstrip().split()

    # Number of contests
    n = int(first_multiple_input[0])
    # Maximum number of important contests Lena can lose
    k = int(first_multiple_input[1])

    contests = []

    # Read the contest data
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    # Compute the result
    result = luckBalance(k, contests)

    # Write the result to output
    fptr.write(str(result) + '\n')

    fptr.close()