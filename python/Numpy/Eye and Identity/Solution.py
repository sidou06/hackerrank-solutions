# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy 

# Set print options for legacy formatting
numpy.set_printoptions(legacy='1.13')

# Read dimensions for identity matrix
n, m = tuple(map(int, input().split()))

# Print identity matrix with given dimensions
print(numpy.eye(n, m))