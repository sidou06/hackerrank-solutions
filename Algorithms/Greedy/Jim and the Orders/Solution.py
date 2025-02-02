#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    # Write your code here
    res = []  # Initialize an empty list to store the total times
    for i in range(len(orders)):  # Iterate over each order
        res.append(orders[i][0] + orders[i][1])  # Calculate the sum of order time and delivery time
    li = range(1, len(res) + 1)  # Generate a list of indices (1-based)
    return sorted(li, key=lambda x: (res[x - 1], x))  # Sort based on the total time, then by index

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read the number of orders

    orders = []  # Initialize the orders list

    for _ in range(n):  # Read the orders
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)  # Call the jimOrders function to get the sorted order

    fptr.write(' '.join(map(str, result)))  # Write the result to the output

    fptr.write('\n')

    fptr.close()  # Close the output file