# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy 

# Initialize lists for storing input arrays
np = []
mp = [] 

# Read dimensions of the arrays
n, m, p = tuple(map(int, input().split()))

# Read first array
for i in range(n):
    np.append(list(map(int, input().split())))

# Convert list to numpy array
np = numpy.array(np) 

# Read second array
for i in range(m):
    mp.append(list(map(int, input().split())))

# Convert list to numpy array
mp = numpy.array(mp) 

# Concatenate both arrays along axis 0
print(numpy.concatenate((np, mp), axis=0))