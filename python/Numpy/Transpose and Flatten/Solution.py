# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy 

# Read the dimensions of the array
n, m = tuple(map(int, input().split()))

# Read the array elements
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

# Convert list to numpy array
s = numpy.array(s) 

# Print the transposed array
print(numpy.transpose(s))

# Print the flattened array
print(s.flatten())