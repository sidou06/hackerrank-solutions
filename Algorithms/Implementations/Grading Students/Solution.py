#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    i = 0  # Initialize index
    for grade in grades:
        # Round grades that are greater than 37 and have a remainder > 2 when divided by 5
        if grade > 37 and grade % 5 > 2:
            grades[i] = grade + 5 - grade % 5  # Round up
        i = i + 1  # Move to next grade
    return grades  # Return the modified list of grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open the output file

    grades_count = int(input().strip())  # Read number of grades

    grades = []  # Initialize an empty list to store grades

    for _ in range(grades_count):
        grades_item = int(input().strip())  # Read each grade
        grades.append(grades_item)  # Append to grades list

    result = gradingStudents(grades)  # Call the grading function

    fptr.write('\n'.join(map(str, result)))  # Write result to the output file
    fptr.write('\n')  # Add newline after writing result

    fptr.close()  # Close the file