# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy 

# Read input and convert to a numpy array
r = numpy.array(list(map(int, input().split())))

# Reshape the array to 3x3
r.shape = (3, 3)

# Print the reshaped array
print(r) 