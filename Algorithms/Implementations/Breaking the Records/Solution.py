#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Initialize the best and worst scores as the first score in the list
    best = scores[0]
    worst = scores[0]
    nb1 = 0  # To count how many times the best score is broken
    nb2 = 0  # To count how many times the worst score is broken
    
    # Loop through the remaining scores
    for i in range(1, len(scores)):
        # Update the best score and increment the count
        if scores[i] > best:
            best = scores[i]
            nb1 += 1
        # Update the worst score and increment the count
        if scores[i] < worst:
            worst = scores[i]
            nb2 += 1
    
    # Return the results as a list
    a = [nb1, nb2]
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of scores
    n = int(input().strip())

    # Read the scores
    scores = list(map(int, input().rstrip().split()))

    # Get the result from the function
    result = breakingRecords(scores)

    # Write the result to the output file
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()