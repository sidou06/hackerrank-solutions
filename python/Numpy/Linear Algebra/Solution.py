# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

# Read the number of rows
n = int(input())

# Initialize the matrix
m = []

# Read the matrix rows
for i in range(n):
    m.append(list(map(float, input().split())))

# Compute the determinant using numpy's linalg.det function
d = np.linalg.det(m)

# Print the determinant rounded to 2 decimal places
print(round(d, 2))