# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy 

# Set numpy print options for legacy formatting
numpy.set_printoptions(legacy='1.13')

# Read input and convert to numpy array of floats
arr = numpy.array(list(map(float, input().split())))

# Print floor, ceil, and rint values of the array
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))