#!/bin/python3

# Import necessary modules
import math
import os
import random
import re
import sys
from itertools import groupby

# Main function
if __name__ == '__main__':
    # Read input string
    s = input()

    # Initialize an empty dictionary to store character frequencies
    dic = {}

    # Count frequency of each character in the string
    for c in s:
        if c in dic:
            dic[c] += 1  # Increment frequency if character already in dictionary
        else:
            dic[c] = 1  # Initialize frequency for new character

    # Sort the dictionary items first by frequency (descending), then by character (ascending), and get top 3
    my_dic = sorted(dic.items(), key = lambda x: (-x[1], x[0]))[:3]

    # Print the top 3 most frequent characters and their frequencies
    for key, value in my_dic:
        print(key + " " + str(value))