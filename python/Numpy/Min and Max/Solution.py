# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy 

# Read input values for n (rows) and m (columns)
n, m = tuple(map(int, input().split()))

# Initialize an empty list to store matrix rows
arr = [] 

# Read n rows of input and append to the list
for i in range(n):
    arr.append(list(map(int, input().split())))

# Convert list to a numpy array
arr = numpy.array(arr) 

# Compute the minimum value along axis 1 (row-wise minimum)
mi = numpy.min(arr, axis=1)

# Compute and print the maximum value among the row-wise minimums
print(numpy.max(mi))