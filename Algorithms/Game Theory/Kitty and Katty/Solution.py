#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # Read number of test cases
    T = int(input().strip())

    # Loop through each test case
    for T_itr in range(T):
        # Read the integer n for the current test case
        n = int(input().strip())

        # Check if n is even or equals 1, print "Kitty" in that case
        if n % 2 == 0 or n == 1:
            print("Kitty")
        else:
            # Otherwise, print "Katty"
            print("Katty")