#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Calculate the actual share Anna should pay
    actual_share = (sum(bill) - bill[k]) // 2
    
    # If the amount Brian charged her is equal to the actual share
    if actual_share == b:
        print("Bon Appetit")
    else:
        # Otherwise, print the difference
        print(b - actual_share)
    return True

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    # Number of items on the bill
    n = int(first_multiple_input[0])

    # Index of the item Anna didn't eat
    k = int(first_multiple_input[1])

    # List of all the bill amounts
    bill = list(map(int, input().rstrip().split()))

    # Amount Brian charged Anna
    b = int(input().strip())

    # Call the bonAppetit function
    bonAppetit(bill, k, b)