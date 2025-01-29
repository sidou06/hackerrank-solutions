# Enter your code here. Read input from STDIN. Print output to STDOUT
s = [] 

# Import numpy for numerical operations
import numpy 

# Read input values for n (rows) and m (columns)
n, m = tuple(map(int, input().split()))

# Read the matrix rows and append them to the list
for i in range(n):
    s.append(list(map(int, input().split())))

# Convert the list to a numpy array
s = numpy.array(s)

# Compute the mean along axis 1 (row-wise mean) and print it
print(numpy.mean(s, axis=1))

# Compute the variance along axis 0 (column-wise variance) and print it
print(numpy.var(s, axis=0))

# Compute the standard deviation of the entire array and round to 11 decimal places
x = numpy.std(s, axis=None)
print(numpy.around(x, 11))