# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the list of coefficients
coeff = list(map(float, input().split()))

# Read the value to substitute in the polynomial
val = float(input())

# Import numpy and calculate the value of the polynomial for the given input
import numpy as np
print(np.polyval(coeff, val))