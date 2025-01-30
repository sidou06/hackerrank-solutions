#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # If the kangaroos have the same velocity
    if v1 == v2:
        if x1 == x2:  # They meet if they start from the same position
            return ("YES")
        else:  # They will never meet if they start at different positions
            return ("NO")
    else:
        # Calculate the number of jumps required for both kangaroos to meet
        a = (x2 - x1) // (v1 - v2)
        if a > 0 and (x2 - x1) % (v1 - v2) == 0:  # They meet if the distance difference is divisible by velocity difference
            return("YES")
        else:  # Otherwise, they will never meet
            return("NO")
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])  # Starting position of kangaroo 1
    v1 = int(first_multiple_input[1])  # Velocity of kangaroo 1
    x2 = int(first_multiple_input[2])  # Starting position of kangaroo 2
    v2 = int(first_multiple_input[3])  # Velocity of kangaroo 2

    result = kangaroo(x1, v1, x2, v2)  # Call the function to check if they meet

    fptr.write(result + '\n')

    fptr.close()