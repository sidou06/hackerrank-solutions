#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'minimumLoss' function below.
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.

def minimumLoss(price):
    # Initialize minimum loss to a large value
    minimum = 10 ** 16
    dic = {}
    # Create a dictionary to store the original indices of the prices
    for i in range(len(price)):
        dic[price[i]] = i 
    # Sort the prices in ascending order
    price.sort()
    # Iterate over the sorted prices in reverse order to find the minimum loss
    for i in range(len(price) - 1, 0, -1):
        # Check if the current price comes before the previous price in the original list
        if dic[price[i]] < dic[price[i - 1]]:
            d = price[i] - price[i - 1]
            # Update the minimum loss if a smaller loss is found
            if d < minimum:
                minimum = d
    return minimum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()