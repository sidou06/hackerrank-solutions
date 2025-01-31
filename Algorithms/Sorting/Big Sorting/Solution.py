#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    # Sort numbers first by length, then lexicographically
    return sorted(unsorted, key=lambda s: (len(s), s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read the number of elements

    unsorted = []  # Initialize the list

    for _ in range(n):
        unsorted_item = input()  # Read each number as a string
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)  # Sort the numbers

    fptr.write('\n'.join(result))  # Write the sorted result to output
    fptr.write('\n')

    fptr.close()