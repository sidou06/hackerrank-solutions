#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'boardCutting' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost_y
#  2. INTEGER_ARRAY cost_x
#
mod = 10 ** 9 + 7
def boardCutting(cost_y, cost_x):
    # Write your code here
    cost_x.sort()  # Sort the x-cut costs in ascending order
    cost_y.sort()  # Sort the y-cut costs in ascending order
    nb_cols = 1  # Start with one column
    nb_lines = 1  # Start with one line
    total = 0  # Initialize the total cost to 0
    m = len(cost_y)  # Number of y cuts
    n = len(cost_x)  # Number of x cuts
    
    while nb_cols <= n and nb_lines <= m:
        coutx = cost_x[-nb_cols]  # Get the cost of the current x cut
        couty = cost_y[-nb_lines]  # Get the cost of the current y cut
        if coutx < couty:  # If x cut cost is less, prioritize y cuts
            nb_lines += 1
            total += (nb_cols * couty)  # Add the cost of the y cut
            total %= mod  # Keep the total cost within the modulo
        else:  # If y cut cost is less or equal, prioritize x cuts
            nb_cols += 1
            total += nb_lines * coutx  # Add the cost of the x cut
            total %= mod  # Keep the total cost within the modulo
    
    while nb_cols <= n:  # If there are remaining x cuts to process
        coutx = cost_x[-nb_cols]  # Get the cost of the current x cut
        nb_cols += 1
        total += nb_lines * coutx  # Add the cost of the x cut
        total %= mod  # Keep the total cost within the modulo
    
    while nb_lines <= m:  # If there are remaining y cuts to process
        couty = cost_y[-nb_lines]  # Get the cost of the current y cut
        nb_lines += 1
        total += nb_cols * couty  # Add the cost of the y cut
        total %= mod  # Keep the total cost within the modulo
    
    return total  # Return the total cost after all cuts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())  # Read the number of test cases

    for q_itr in range(q):  # Process each test case
        first_multiple_input = input().rstrip().split()

        m = int(first_multiple_input[0])  # Read the number of rows
        n = int(first_multiple_input[1])  # Read the number of columns

        cost_y = list(map(int, input().rstrip().split()))  # Read the y cut costs
        cost_x = list(map(int, input().rstrip().split()))  # Read the x cut costs

        result = boardCutting(cost_y, cost_x)  # Call the function to get the result

        fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file