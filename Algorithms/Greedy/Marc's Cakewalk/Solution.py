#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    # Sort the calorie list in descending order to minimize miles
    calorie.sort()
    calorie.reverse()
    
    # Initialize variables for power of 2 multiplier and total miles
    j = 1
    miles = 0
    
    # Iterate through the sorted calorie list
    for k in calorie:
        miles += j * k  # Add the current calorie * power of 2
        j *= 2  # Double the power of 2 for the next element
    
    return miles 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read number of cupcakes
    n = int(input().strip())

    # Read calorie values
    calorie = list(map(int, input().rstrip().split()))

    # Compute the minimum miles required
    result = marcsCakewalk(calorie)

    # Write the result to output
    fptr.write(str(result) + '\n')

    fptr.close()