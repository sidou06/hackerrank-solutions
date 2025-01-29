# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

# Read the first array a
a = np.array(list(map(int, input().split())))

# Read the second array b
b = np.array(list(map(int, input().split())))

# Print the inner product of a and b
print(np.inner(a, b))

# Print the outer product of a and b
print(np.outer(a, b))