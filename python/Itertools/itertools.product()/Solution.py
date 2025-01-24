# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools 
from itertools import product 

# Read and process the first input list
A = input().rstrip().split()
a = [int(nb) for nb in A]

# Read and process the second input list
B = input().rstrip().split() 
b = [int(nb) for nb in B]

# Generate the Cartesian product of the two lists
p = list(product(a, b))

# Print the Cartesian product, separated by spaces
print(*p, sep=" ")