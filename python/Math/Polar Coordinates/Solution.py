# Enter your code here. Read input from STDIN. Print output to STDOUT

import cmath 

# Read the complex number as a string
n = input() 

# Initialize variables
k = 0
sign = 1 

# Check for negative sign in the real part
if n[0] == "-":
    sign = -1 
    k += 1

# Extract the real part of the complex number
i = ""
while n[k] != "+" and n[k] != "-":
    i = i + n[k]
    k += 1

# Initialize the sign for the imaginary part
sign2 = 1 

# Check for negative sign in the imaginary part
if n[k] == "-":
    sign2 = -1
k += 1 

# Convert the real part to an integer
i = int(i) * sign 

# Extract the imaginary part
j = ""
while n[k] != "j":
    j = j + n[k]  
    k += 1

# Convert the imaginary part to an integer
j = int(j) * sign2 

# Compute and print the modulus (absolute value) of the complex number
print(abs(complex(i, j))) 

# Compute and print the phase (angle) of the complex number
print(cmath.phase(complex(i, j)))