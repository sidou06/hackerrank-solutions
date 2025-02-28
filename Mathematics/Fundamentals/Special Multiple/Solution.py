#!/bin/python3

import math
import os
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def next_num(x):
    ch = str(x)  # Convert number to string
    done = False  # Flag to track if modification is done
    j = len(ch) - 1  # Start from the last digit
    res = x  # Initialize result with x
    
    while (done == False) and (j >= 0):  # Iterate through digits from right to left
        if ((res // (10**(len(ch) - 1 - j))) % 10) == 9:  # If the digit is 9
            res = res - (9 * (10**(len(ch) - 1 - j)))  # Replace 9 with 0
        else:
            res = res + (9 * (10**(len(ch) - 1 - j)))  # Replace digit with 9
            done = True  # Stop modification
        j = j - 1  # Move to next digit
    
    if (done == False):  # If all digits were 9s
        return 9 * (10**len(ch))  # Return next power of 10
    
    return res

def solve(n):
    x = 9  # Start with 9
    while (x % n) != 0:  # Find the smallest multiple of n
        x = next_num(x)  # Generate next number with only 0s and 9s
    return str(x)  # Return result as string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        n = int(input().strip())  # Read input value

        result = solve(n)  # Compute result

        fptr.write(result + '\n')  # Write output

    fptr.close()