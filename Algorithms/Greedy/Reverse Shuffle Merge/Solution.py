#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter

def reverseShuffleMerge(s):

    # Step 1: Count character frequencies
    freq = Counter(s)  # Total frequencies in s
    required = {char: count // 2 for char, count in freq.items()}  # Needed for A
    used = {char: 0 for char in freq}  # Track used characters in reverse(A)

    stack = []  # Stack to build reverse(A)

    # Step 2: Traverse from right to left
    for char in reversed(s):
        # If this character is still needed in A
        if used[char] < required[char]:
            # Ensure lexicographical order
            while stack and stack[-1] > char and used[stack[-1]] + freq[stack[-1]] - 1 >= required[stack[-1]]:
                removed_char = stack.pop()
                used[removed_char] -= 1

            # Add current character to stack
            stack.append(char)
            used[char] += 1

        # Decrease the frequency (since we're processing the string)
        freq[char] -= 1

    # Step 3: Reverse the stack to get A
    return ''.join(stack)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()