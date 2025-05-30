#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#
alpha_dict = {'a' : 0,
              'b' : 1,
              'c' : 2,
              'd' : 3,
              'e' : 4,
              'f' : 5,
              'g' : 6,
              'h' : 7,
              'i' : 8,
              'j' : 9,
              'k' : 10,
              'l' : 11,
              'm' : 12,
              'n' : 13,
              'o' : 14,
              'p' : 15,
              'q' : 16,
              'r' : 17,
              's' : 18,
              't' : 19,
              'u' : 20,
              'v' : 21,
              'w' : 22,
              'x' : 23,
              'y' : 24,
              'z' : 25}

def designerPdfViewer(h, word):
    # Write your code here
    maxi = 0
    for c in word:
        if h[alpha_dict[c]] > maxi:
            maxi = h[alpha_dict[c]]
    return maxi * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()