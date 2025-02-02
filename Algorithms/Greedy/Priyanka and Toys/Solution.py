#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w):
    # Sort the weights in ascending order
    w.sort()
    
    # Initialize the number of containers required
    res = 0
    
    # Process the list until all weights are assigned to containers
    while len(w) > 0:
        # Take the minimum weight as the base for a container
        mi = w[0]
        
        # Remove all toys that fit within the weight range of mi to mi + 4
        while len(w) > 0 and w[0] <= mi + 4:
            w.pop(0)
        
        # Increment the container count
        res += 1
    
    # Return the total number of containers used
    return res 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of toys
    n = int(input().strip())

    # Read the weights of the toys
    w = list(map(int, input().rstrip().split()))

    # Compute the minimum number of containers needed
    result = toys(w)

    # Write the result to output
    fptr.write(str(result) + '\n')

    fptr.close()