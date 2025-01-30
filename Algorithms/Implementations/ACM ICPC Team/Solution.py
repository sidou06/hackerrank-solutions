#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Initialize the variables to track the maximum topics known and number of teams
    nbteams = 0
    maxtopics = 0
    
    # Loop through each pair of teams
    for i in range(len(topic) - 1):
        for j in range(i + 1, len(topic)):
            team1 = topic[i]
            team2 = topic[j]
            known = 0
            
            # Count the topics known by either team in the pair
            for k in range(len(team1)):
                if team1[k] == '1' or team2[k] == '1':
                    known += 1
            
            # Update the maximum topics known and the number of teams achieving it
            if known > maxtopics:
                maxtopics = known
                nbteams = 1
            elif known == maxtopics:
                nbteams += 1
    
    # Return the result: maximum topics and the number of teams achieving it
    return [maxtopics, nbteams]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input values
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    topic = []

    # Read each team's known topics
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    # Get the result and write to output
    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()