#!/bin/python3

import math
import os
import random
import re
import sys

def minimumPasses(m, w, p, n):
    # Initialize variables
    days = 0  # Number of days taken to accumulate enough candies
    candies = 0  # Total number of candies we have
    answer = math.ceil(n / (m * w))  # Initial estimate of the minimum number of days needed

    while days < answer:
        # If we don't have enough candies to buy another machine, calculate how many days are needed
        if p > candies:
            daysNeeded = math.ceil((p - candies) / (m * w))  # Calculate how many days to collect enough candies
            candies += daysNeeded * m * w  # Collect candies
            days += daysNeeded  # Increment the days

        # Calculate the difference between machines and available candies
        diff = abs(m - w)
        available = candies // p  # Calculate how many machines we can afford with the current candies
        purchased = min(diff, available)  # Buy as many machines as the difference between m and w

        # Update m and w based on which one is smaller
        if m < w:
            m += purchased  # Upgrade m if it is smaller
        else:
            w += purchased  # Upgrade w if it is smaller

        # Distribute the remaining available candies evenly between m and w
        rest = available - purchased
        m += rest // 2  # Distribute half of the remaining candies to m
        w += rest - rest // 2  # Distribute the other half to w

        candies -= available * p  # Deduct the candies used to purchase machines
        candies += m * w  # Add new candies produced by the updated machines
        days += 1  # Increment the day count

        # Calculate the remaining candies needed and update the minimum days required
        remainigCandies = max(n - candies, 0)  # Calculate remaining candies needed to reach the target
        answer = min(answer, days + math.ceil(remainigCandies / (m * w)))  # Update answer if this method takes fewer days

    return answer  # Return the final answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values for m, w, p, and n
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])  # Number of machines (m)
    w = int(first_multiple_input[1])  # Number of workers (w)
    p = int(first_multiple_input[2])  # Cost to purchase one machine (p)
    n = int(first_multiple_input[3])  # Total number of candies needed (n)

    # Calculate the result
    result = minimumPasses(m, w, p, n)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    fptr.close()    