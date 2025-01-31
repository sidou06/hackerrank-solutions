#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagrams(liste, w):
    cpt = 0
    for word in liste:
        anag = True 
        j = 0
        while j < len(word) and anag:
            if word.count(word[j]) != w.count(word[j]):
                anag = False
            j += 1
        if anag: 
            cpt += 1
    return cpt
    
def sherlockAndAnagrams(s):
    # Write your code here
    cpt = 0 
    for l in range(1, len(s)):  # Check all possible substring lengths
        for k in range(len(s) - l):  # Iterate through all possible starting points
            a = s[k:k + l]  # Substring of length l starting at index k
            lis = []  # List to store substrings of length l
            for m in range(k + 1, len(s) - l + 1):  # Iterate through the remaining substrings
                lis.append(s[m:m + l])  # Append substring to list
            cpt += anagrams(lis, a)  # Count the anagrams in the list
    return cpt  # Return the total count of anagram pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())  # Number of test cases

    for q_itr in range(q):
        s = input()  # Input string

        result = sherlockAndAnagrams(s)  # Call the function to get the result

        fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()