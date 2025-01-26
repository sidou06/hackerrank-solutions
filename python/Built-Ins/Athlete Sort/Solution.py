#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()  # Read the dimensions of the array

    n = int(nm[0])  # Number of rows
    m = int(nm[1])  # Number of columns

    arr = []  # Initialize the array

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))  # Read each row of the array

    k = int(input())  # Read the column index to sort by
    arr = sorted(arr, key=lambda x: x[k])  # Sort the array based on the k-th column

    for ele in arr:
        print(" ".join(str(nb) for nb in ele))  # Print the sorted array row by row