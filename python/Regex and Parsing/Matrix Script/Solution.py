#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

s = ""
for i in range(m):
    for j in range(n):
        s += matrix[j][i]
import re 
reg = r'([a-zA-Z0-9])(\W+)([a-zA-Z0-9])'
print(re.sub(reg,r'\1 \3', s))
