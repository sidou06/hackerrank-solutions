#!/bin/python3

import sys

if __name__ == '__main__':
    t = int(input().strip())  # Read the number of test cases
    for a0 in range(t):
        
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])  # Read the value of n
        k = int(first_multiple_input[1])  # Read the value of k

        # Check if k is in the first half range
        if k <= (n - 2) // 2:
            print(1 + 2 * k)  # Compute and print the result for first condition
        else:
            print((n - k - 1) * 2)  # Compute and print the result for second condition