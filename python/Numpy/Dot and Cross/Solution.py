# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

# Read the number of rows/columns for the matrices
n = int(input())

# Initialize lists to store the two matrices
a = [] 
b = [] 

# Read the first matrix a
for i in range(n):
    a.append(list(map(int, input().split())))

# Read the second matrix b
for i in range(n):
    b.append(list(map(int, input().split())))

# Convert the lists to numpy arrays for matrix operations
a = np.array(a)
b = np.array(b)

# Compute the dot product of matrices a and b
c = np.dot(a, b)

# Print the result
print(c)