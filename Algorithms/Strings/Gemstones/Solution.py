#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    # Write your code here
    count = 0  # Initialize the count of gemstones
    alpha = "abcdefghijklmnopqrstuvwxyz"  # List of all lowercase letters (alphabets)

    # Iterate over each letter of the alphabet
    for i in range(26):
        gems = True  # Flag to track if the current letter is a gemstone
        j = 0  # Initialize the index to iterate through the array
        while j < len(arr) and gems:  # Iterate through each string in the array
            if alpha[i] not in arr[j]:  # If the current letter is not in the string
                gems = False  # Set gems to False and break out of the loop
            j += 1  # Move to the next string
        if gems:  # If the letter is found in all strings
            count += 1  # Increment the gemstone count
    return count  # Return the total number of gemstones

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read the number of strings

    arr = []  # Initialize an empty list to store the strings

    # Read the strings and append them to the list
    for _ in range(n):
        arr_item = input()  # Read the string
        arr.append(arr_item)  # Append it to the list

    result = gemstones(arr)  # Call the gemstones function

    fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file