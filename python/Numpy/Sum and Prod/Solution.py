# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np 

# Read input values for n (rows) and m (columns)
n, m = tuple(map(int, input().split()))

# Initialize an empty list to store matrix rows
s = []

# Read n rows of input and append to the list
for i in range(n):
    s.append(list(map(int, input().split())))

# Convert list to a numpy array
s = np.array(s)

# Compute the sum along axis 0 (column-wise sum)
line = np.sum(s, axis=0)

# Compute and print the product of the summed values
print(np.prod(line))