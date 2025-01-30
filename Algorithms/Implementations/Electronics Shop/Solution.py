#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    # Initialize the maximum amount of money spent as -1
    act = -1

    # Iterate through each combination of keyboard and drive
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            # Check if the total cost of a keyboard and drive is within the budget and greater than the current maximum
            if b >= keyboards[i] + drives[j] > act:
                act = keyboards[i] + drives[j]

    # Return the maximum amount of money spent, or -1 if no valid combination is found
    return act

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read inputs
    bnm = input().split()

    b = int(bnm[0])  # Budget
    n = int(bnm[1])  # Number of keyboards
    m = int(bnm[2])  # Number of drives

    # Lists of keyboard and drive prices
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    # Calculate the maximum money spent on a valid keyboard and drive combination
    moneySpent = getMoneySpent(keyboards, drives, b)

    # Output the result
    fptr.write(str(moneySpent) + '\n')

    fptr.close()