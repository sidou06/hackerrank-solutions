#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theGreatXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER x as parameter.
#

def theGreatXor(x):
    # Compute the smallest power of 2 greater than x
    power_of_2 = 2 ** (math.ceil(math.log2(x + 1)))
    
    # Compute the result by subtracting x from (power_of_2 - 1)
    return power_of_2 - 1 - x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())  # Read number of test cases

    for q_itr in range(q):
        x = int(input().strip())  # Read input value

        result = theGreatXor(x)  # Compute the result

        fptr.write(str(result) + '\n')  # Write result to output

    fptr.close()