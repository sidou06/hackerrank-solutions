#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    # Initialize the number of games to 0
    nb = 0
    
    # Set the initial price of the game to p
    price = p
    
    # Set the budget to s
    budget = s 
    
    # While the budget is enough to buy a game
    while budget >= price:
        # Increment the number of games bought
        nb += 1
        
        # Deduct the current price from the budget
        budget = budget - price
        
        # Decrease the price by d for the next game
        price = price - d
        
        # Ensure the price does not go below the minimum price m
        if price < m:
            price = m
    
    # Return the total number of games that can be bought
    return nb

if __name__ == '__main__':
    # Open the output file for writing the result
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input values
    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    # Call the function to calculate how many games can be bought
    answer = howManyGames(p, d, m, s)

    # Write the result to the output file
    fptr.write(str(answer) + '\n')

    # Close the output file
    fptr.close()