#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    # Initialize variables: 'act' is the current value of the counter, and 'som' is the cumulative time
    act = som = 3
    
    # Loop to simulate the behavior of the strange counter
    while t > som:  # Keep looping until the time 't' is within the current cycle
        act *= 2  # The counter value doubles after each full cycle
        som += act  # Add the duration of the current cycle to 'som' (total time passed)
    
    # After exiting the loop, 'som' holds the end time of the cycle that includes 't'.
    som -= act  # Adjust 'som' to be the time right before the current cycle.
    act -= t - som - 1  # Calculate the remaining counter value for the current cycle
    
    return act  # Return the counter value at time 't'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read the input time 't'

    result = strangeCounter(t)  # Call the function to get the counter value at time 't'

    fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()