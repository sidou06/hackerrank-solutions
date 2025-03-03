#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def solve(c):
    mod = 10 ** 9 + 7  # Define modulo constant
    
    # Initialize a list to store the frequency of elements
    rep = []  
    for i in range(len(c) + 1):  
        rep.append(0)  # Initialize all elements to 0
    
    # Count occurrences of each number in c
    for i in range(len(c)):  
        rep[c[i]] += 1  
    
    # Create an accumulated frequency list
    acc = [rep[0]]  
    for i in range(1, len(rep)):  
        acc.append(acc[i - 1] + rep[i])  
    
    pr = 1  # Initialize product variable
    
    # Compute the product using the accumulated frequency list
    for i in range(len(acc) - 1):  
        pr *= (acc[i] - i)  
        pr = pr % mod  # Apply modulo operation to keep numbers within limit
    
    if pr < 0:  
        return 0  # Return 0 if the product is negative
    
    return pr  # Return final result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        c_count = int(input().strip())  # Read number of elements in array

        c = list(map(int, input().rstrip().split()))  # Read array elements

        result = solve(c)  # Call function to compute result

        fptr.write(str(result) + '\n')  # Write result to output file

    fptr.close()  # Close the file