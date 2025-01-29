# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy 

# Read dimensions of matrices
n, m = tuple(map(int, input().split()))

# Read first matrix
n1 = [list(map(int, input().split())) for _ in range(n)]

# Read second matrix
n2 = [list(map(int, input().split())) for _ in range(n)] 

# Convert lists to numpy arrays
n1 = numpy.array(n1, int)
n2 = numpy.array(n2, int)

# Perform and print element-wise operations
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 // n2) 
print(n1 % n2)
print(n1 ** n2)