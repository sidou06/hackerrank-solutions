# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy 

# Read shape dimensions
shape = tuple(map(int, input().split()))

# Print zero array of given shape
print(numpy.zeros(shape, dtype=numpy.int))

# Print ones array of given shape
print(numpy.ones(shape, dtype=numpy.int))