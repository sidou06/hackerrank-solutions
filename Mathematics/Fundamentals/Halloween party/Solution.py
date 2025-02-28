#!/bin/python3

import math
import os
import sys

#
# Complete the 'halloweenParty' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER k as parameter.
#

def halloweenParty(k):
    return (k // 2) * (k - k // 2)  # Compute the maximum number of pieces by dividing k into two parts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for t_itr in range(t):
        k = int(input().strip())  # Read k value

        result = halloweenParty(k)  # Compute result

        fptr.write(str(result) + '\n')  # Write output

    fptr.close()