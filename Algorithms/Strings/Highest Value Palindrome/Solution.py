#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    l = list(s)  # Convert string to list to modify characters
    c = 0  # Count the number of non-matching character pairs
    for i in range(n // 2):  # Compare the characters from both ends
        if l[i] != l[n - i - 1]:
            c += 1  # Increment if characters don't match
    if c > k:  # If there are more non-matching pairs than available changes, return -1
        return "-1"
    
    # Try to create the largest possible palindrome
    for i in range(n // 2):
        if l[i] == l[n - i - 1]:  # If the characters match
            if l[i] != "9" and k - 2 >= c:  # If we can change both characters to '9'
                l[i] = "9"
                l[n - i - 1] = "9"
                k -= 2  # Decrease k by 2 as we used two changes
        else:  # If the characters don't match
            if max(l[i], l[n - i - 1]) == "9":  # If one of the characters is '9'
                l[i] = "9"
                l[n - i - 1] = "9"
                k -= 1  # Decrease k by 1 as we used one change
                c -= 1  # Decrease the non-matching count as we've fixed the pair
            else:  # If neither character is '9'
                if k - 2 >= c - 1:  # If we can afford two changes
                    l[i] = "9"
                    l[n - i - 1] = "9"
                    k -= 2  # Decrease k by 2 as we used two changes
                    c -= 1  # Decrease the non-matching count
                else:  # Otherwise, choose the larger of the two characters
                    m = max(l[i], l[n - i - 1])
                    l[i] = m
                    l[n - i - 1] = m
                    k -= 1  # Decrease k by 1
                    c -= 1  # Decrease the non-matching count
    
    if n % 2 == 1 and k > 0:  # If the length is odd and we have remaining changes
        l[n // 2] = "9"  # Change the middle character to '9'
    
    return "".join(ele for ele in l)  # Convert list back to string and return

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()