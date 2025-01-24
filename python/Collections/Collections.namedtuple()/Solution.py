# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

# Input number of students
n = int(input().rstrip())

# Initialize total marks
s = 0

# Define the namedtuple for student with the given column names
student = namedtuple('student', input().rstrip())

# Process each student's data
for i in range(n):
    li = input().rstrip().split()
    stud = student(li[0], li[1], li[2], li[3])  # Create a student namedtuple
    s += int(stud.MARKS)  # Add the marks to the total

# Calculate and print the average marks
s /= n
print(s)