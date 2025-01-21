#!/bin/python3

import math
import os
import random
import re
import sys

# Main execution block
if __name__ == '__main__':
    # Read an integer input from the user and strip any extra whitespace
    n = int(input().strip())
    
    # Check if the number is odd OR if it falls in the range 6 to 20 (inclusive)
    if n % 2 == 1 or 6 <= n <= 20:
        print("Weird")  # Output "Weird" for odd numbers or numbers in the range 6 to 20
    else:
        print("Not Weird")  # Output "Not Weird" for all other cases