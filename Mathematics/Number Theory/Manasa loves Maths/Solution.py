#!/bin/python3

import math  # Importing math module for mathematical operations
import os  # Importing os module for environment operations
import random  # Importing random module (not used in this code)
import re  # Importing re module for regular expressions (not used in this code)
import sys  # Importing sys module for system-specific parameters

# List of valid two-digit numbers that are divisible by 8
twos = [[0,0],[0,8],[1,6],[2,4],[3,2],[4,0],[4,8],[5,6],[6,4],[7,2],[8,0],[8,8],[9,6]] 
two = []  # List to store extended two-digit combinations
for i in range(13):  # Iterating through predefined two-digit numbers
    x = twos[i]  # Extracting the current list
    for j in range(5):  # Adding multiples of 2 up to 8
        x.append(2 * j)  # Appending even numbers
        c = x.copy()  # Creating a copy of the list
        two.append(c)  # Adding the copy to the main list
        x.pop()  # Removing last appended value

# List of valid two-digit numbers that contribute to three-digit numbers divisible by 8
threes = [[0,4],[1,2],[2,0],[2,8],[3,6],[4,4],[5,2],[6,0],[6,8],[7,6],[8,4],[9,2]]
three = []  # List to store extended three-digit combinations
for i in range(12):  # Iterating through predefined two-digit numbers
    x = threes[i]  # Extracting the current list
    for j in range(5):  # Adding odd multiples up to 9
        x.append(2 * j + 1)  # Appending odd numbers
        c = x.copy()  # Creating a copy of the list
        three.append(c)  # Adding the copy to the main list
        x.pop()  # Removing last appended value
        
def solve(n):  
    # Function to determine if a number is divisible by 8
    li = []  # List to store integer digits of input number
    for c in n:  # Iterating through each character in input string
        li.append(int(c))  # Converting character to integer and storing
    if len(li) == 1:  # If single-digit number
        if li[0] == 0 or li[0] == 8:  # Check if it's 0 or 8
            return "YES"  # It is divisible by 8
        else:
            return "NO"  # Not divisible by 8
    elif len(li) == 2:  # If two-digit number
        for i in range(len(twos)):  # Checking predefined two-digit combinations
            if all(twos[i].count(elem) <= li.count(elem) for elem in set(twos[i])):
                return "YES"  # Found a match that is divisible by 8
        return "NO"  # No valid match found
    else:  # If three or more digits
        for i in range(len(two)):  # Checking predefined extended two-digit combinations
            if all(two[i].count(elem) <= li.count(elem) for elem in set(two[i])):
                return "YES"  # Found a match
        for i in range(len(three)):  # Checking predefined extended three-digit combinations
            if all(three[i].count(elem) <= li.count(elem) for elem in set(three[i])):
                return "YES"  # Found a match
        return "NO"  # No valid match found
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Opening output file

    t = int(input().strip())  # Reading number of test cases

    for t_itr in range(t):  # Iterating through test cases
        n = input()  # Reading input number

        result = solve(n)  # Solving for current number

        fptr.write(result + '\n')  # Writing result to output file

    fptr.close()  # Closing output file
