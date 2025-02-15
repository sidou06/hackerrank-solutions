#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Reverse the array in place
    a.reverse() 
    return a 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of elements in the array
    arr_count = int(input().strip())

    # Read the array elements as a list of integers
    arr = list(map(int, input().rstrip().split()))

    # Reverse the array
    res = reverseArray(arr)

    # Write the reversed array to output
    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()