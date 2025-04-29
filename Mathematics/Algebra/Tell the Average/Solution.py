# Read number of elements
n = int(input())

# Read list of integers
l = list(map(int, input().split()))

# Initialize product result
p = 1 

# Define modulo value
m = 10 ** 9 + 7

# Iterate through each element in the list
for ele in l:
    # Multiply (ele + 1) to product
    p *= (ele + 1)
    # Take modulo to prevent overflow
    p %= m 

# Subtract 1 to exclude empty subset
print(p - 1)
