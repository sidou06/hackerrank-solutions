#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def get_power(n):
    # Find the highest power of 2 less than or equal to n
    power = 0
    k = 1
    while 2 * k <= n:
        k = k * 2
        power += 1
    return power
    
    
def counterGame(n):
    d = 0  # Counter for the number of moves
    while n % 2 == 0:  # Check if n is a power of 2
        d += 1
        n //= 2  # Reduce n by dividing it by 2
    
    while n > 1:
        if n % 2:  # If n is odd, increase the counter
            d += 1
        n //= 2  # Reduce n by dividing it by 2
    
    # If the number of moves is even, Richard wins; otherwise, Louise wins
    if d % 2 == 0:
        return("Richard")
    return("Louise")
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        n = int(input().strip())  # Read the game number

        result = counterGame(n)  # Determine the winner

        fptr.write(result + '\n')  # Write the result to output

    fptr.close()