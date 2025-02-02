#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Sort the prices in ascending order
    prices.sort() 
    
    res = 0
    i = 0
    
    # Continue buying toys while we have enough money
    while i < len(prices) and k >= prices[i]:
        k -= prices[i]  # Deduct the price of the current toy
        i += 1  # Move to the next toy
        res += 1  # Increase the count of toys bought
        
    return res  # Return the total number of toys bought

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input values
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])  # Number of toys
    k = int(first_multiple_input[1])  # Total money available

    prices = list(map(int, input().rstrip().split()))  # Prices of the toys

    # Get the result of maximum toys that can be bought
    result = maximumToys(prices, k)

    # Write the result to output
    fptr.write(str(result) + '\n')

    fptr.close()