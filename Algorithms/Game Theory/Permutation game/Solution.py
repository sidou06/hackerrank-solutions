#!/bin/python3

import math
import os
import random
import re
import sys

from functools import cache

#
# Complete the 'permutationGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def permutationGame(arr):
    # Check if the remaining array is sorted in increasing order
    def is_increasing(remain):
        # Iterate over the array and check if each element is smaller than the next
        return all(remain[i] < remain[i+1] for i in range(len(remain)-1))
    
    # Generate a new permutation by removing an element
    def new_perm(remain, removed):
        # For each element in remain, decrease the value if it's greater than the removed element
        # and exclude the removed element from the list
        return tuple(e - 1 if e > removed else e for e in remain if e != removed)

    # Recursive function to check if the first player can win
    @cache
    def first_wins(remain):
        # If the array is in increasing order, the second player wins
        if is_increasing(remain):
            return False
        # Otherwise, check if there exists a move that leads to the second player losing
        return any(not first_wins(new_perm(remain, e)) for e in remain)

    # Return 'Alice' if the first player wins, else 'Bob'
    return 'Alice' if first_wins(tuple(arr)) else 'Bob'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Number of test cases
    t = int(input().strip())

    # Iterate over each test case
    for t_itr in range(t):
        # Number of elements in the array
        arr_count = int(input().strip())

        # Read the array
        arr = list(map(int, input().rstrip().split()))

        # Get the result of the game
        result = permutationGame(arr)

        # Write the result to the output
        fptr.write(result + '\n')

    # Close the output file
    fptr.close()