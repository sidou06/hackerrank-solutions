#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def solve(a):
    # Calculate the total number of passengers
    Total_Passengers = sum(a)
    
    # Initialize the result list with the total passenger count
    Final_Output = [Total_Passengers]
    
    # Iterate over possible bus sizes from 2 up to the maximum valid divisor
    for i in range(2, Total_Passengers // max(a) + 1):
        Current_Size = Total_Passengers // i  # Calculate the current bus size
        j = 0  # Index to traverse the array
        going = False  # Flag to determine if partitioning is possible
        
        # Check if the total number of passengers is evenly divisible
        if Total_Passengers % i == 0:
            going = True
        
        # Try to form groups of size Current_Size
        while j < len(a) and going == True:
            total = 0  # Temporary sum for a group
            
            # Keep adding passengers until reaching the required size
            while total < Current_Size:
                total = total + a[j]
                j = j + 1
            
            # If the sum exceeds the required size, partitioning is not possible
            if total > Current_Size:
                going = False
        
        # If a valid partitioning was found, add the bus size to the result list
        if going == True:
            Final_Output.append(Current_Size)
    
    # Sort the output list before returning
    Final_Output.sort()
    
    return Final_Output
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of elements in the array
    a_count = int(input().strip())

    # Read the array elements
    a = list(map(int, input().rstrip().split()))

    # Get the result from the function
    result = solve(a)

    # Write the result to output
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()