#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    nb1 = nb2 = 0  # Initialize counters for apples and oranges
    for apple in apples:  # Loop through apples
        if s <= apple + a <= t:  # Check if the apple falls within the range
            nb1 += 1  # Increment apple count
    for orange in oranges:  # Loop through oranges
        if s <= orange + b <= t:  # Check if the orange falls within the range
            nb2 += 1  # Increment orange count
    print(nb1)  # Print the number of apples that fall within the range
    print(nb2)  # Print the number of oranges that fall within the range
    return True  # Return True indicating the function completed successfully

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])  # Start of the house
    t = int(first_multiple_input[1])  # End of the house

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])  # Location of the apple tree
    b = int(second_multiple_input[1])  # Location of the orange tree

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])  # Number of apples
    n = int(third_multiple_input[1])  # Number of oranges

    apples = list(map(int, input().rstrip().split()))  # List of distances of apples from the tree

    oranges = list(map(int, input().rstrip().split()))  # List of distances of oranges from the tree

    countApplesAndOranges(s, t, a, b, apples, oranges)  # Call the function with the input parameters