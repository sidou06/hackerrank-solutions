#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def steadyGene(gene):
    # Initialize variables
    i = 0
    n = len(gene)
    j = n - 1
    minl = n
    cnt = {"A": 0, "C": 0, "T": 0, "G": 0}

    # Loop to balance the gene counts
    while True:
        if j < 0 or cnt[gene[j]] == n // 4:
            j += 1
            break
        else:
            cnt[gene[j]] += 1
            j -= 1

    # Track the minimum length of subarray to balance the gene
    if j < minl:
        minl = j

    # Iterate through the gene sequence
    for i in range(n):
        cnt[gene[i]] += 1
        while j < n and cnt[gene[i]] > n // 4:
            cnt[gene[j]] -= 1
            j += 1
        if j == n:
            break
        if j - i - 1 < minl:
            minl = j - i - 1

    return minl  # Return the minimum length of the steady gene subarray

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Input length of gene

    gene = input()  # Input gene sequence

    result = steadyGene(gene)  # Call the function to find the steady gene subarray length

    fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()