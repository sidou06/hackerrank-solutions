#!/bin/python3

import math  # Importing math module for mathematical operations
import os  # Importing os module for environment operations
import random  # Importing random module (not used in this code)
import re  # Importing re module for regular expressions (not used in this code)
import sys  # Importing sys module for system-specific parameters

# Function to factorize a given number x
def factorize(x):
    f = []  # List to store factors
    while x % 2 == 0:  # Checking divisibility by 2
        f.append(2)  # Appending 2 to the list of factors
        x //= 2  # Dividing x by 2
    for i in range(3, int(math.sqrt(x)) + 1, 2):  # Checking odd numbers up to sqrt(x)
        while x % i == 0:  # Checking divisibility by i
            f.append(i)  # Appending i to the list of factors
            x //= i  # Dividing x by i
    if x > 1:  # If x is still greater than 1, it is a prime factor
        f.append(x)  # Appending the remaining prime factor
    return f  # Returning the list of factors
    
# Function to calculate the longest sequence based on factorization
def longestSequence(a):
    su = 0  # Variable to store the sum of computed values
    for i in range(len(a)):  # Looping through each element in the array
        factors = factorize(a[i])  # Getting the factorized list of the current element
        cu = 1  # Initializing product variable
        for j in range(1, len(factors) + 1):  # Looping through the factors in reverse order
            cu *= factors[-j]  # Multiplying factors in reverse order
            su += cu  # Adding the product to the sum
        su += 1  # Adding 1 to the sum after processing all factors
    return su  # Returning the final sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Opening output file for writing
   
    n = int(input().strip())  # Reading input integer

    a = list(map(int, input().rstrip().split()))  # Reading input list of integers

    result = longestSequence(a)  # Calling the function to compute the result

    fptr.write(str(result) + '\n')  # Writing the result to the output file

    fptr.close()  # Closing the output file