#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter  # Import Counter to count occurrences of elements

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def solve(a):
    total = 0  # Initialize total sum
    
    # Count occurrences of each number in the array
    c = Counter(a)  
    
    # Iterate through the counts of each unique number
    for rep in c.values():
        total += rep * (rep - 1)  # Compute number of pairs for each unique number
    
    return total  # Return the final count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        a_count = int(input().strip())  # Read the number of elements in the array

        a = list(map(int, input().rstrip().split()))  # Read the array elements

        result = solve(a)  # Call the function to compute result

        fptr.write(str(result) + '\n')  # Write result to output file

    fptr.close()  # Close the file