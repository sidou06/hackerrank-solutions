#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Initialize the maximum alternating length
    cpt = 0
    
    # Store unique characters from the string
    let = []  
    for c in s:
        if c not in let:
            let.append(c)  
    
    # Iterate over all pairs of unique characters
    for i in range(len(let) - 1):
        for j in range(i + 1, len(let)):
            count = 0
            stop = False  
            k = 0  
            find = let[i]  
            
            # Traverse the string while ensuring alternating characters
            while k < len(s) and not stop:
                if s[k] not in [let[i], let[j]]:  # Skip characters not in the selected pair
                    k += 1
                elif s[k] == find:  # Check if the character matches the expected alternating character
                    if find == let[i]:  
                        find = let[j]  
                    else:
                        find = let[i]  
                    count += 1
                    k += 1
                else:  # If sequence is broken, stop checking
                    stop = True  
            
            # Update the maximum alternating sequence length
            if not stop and count > cpt:  
                cpt = count  
    
    return cpt  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())  # Read the length of the string

    s = input()  # Read the input string

    result = alternate(s)  # Compute the maximum alternating character sequence

    fptr.write(str(result) + '\n')  # Write the result to output file

    fptr.close()  # Close the output file