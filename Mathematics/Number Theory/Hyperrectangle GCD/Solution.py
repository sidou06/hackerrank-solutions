from math import ceil  # Import ceil function from math module

# Function to compute the greatest common divisor (GCD) using Euclidean algorithm
def gcd(a, b):
    if a > b:
        return gcd(b, a)  # Ensure a is always smaller or equal to b
    while a != 0:
        a, b = b % a, a  # Apply Euclidean algorithm for GCD
    return b

# Function to compute the product of a list modulo 10^9 + 7
def product(lst):
    prod = 1
    for n in lst:
        prod = (prod * n) % (10 ** 9 + 7)  # Compute product modulo 10^9 + 7
    return prod
    
# Global variables
bounds = None  # Global variable to store bounds
cache = None  # Global cache to store computed values
    
# Function to count coprimes for a given divisor
def coprime_count(divisor):
    if divisor > bounds[-1] // 2:
        return 1  # Base case: if divisor is greater than half of max bound
    if divisor in cache:
        return cache[divisor]  # Return cached value if available
    
    # Scale bounds by divisor
    scaled_bounds = [n // divisor for n in bounds]  # Compute new bounds by integer division
    total = product(scaled_bounds)  # Compute product of scaled bounds
    cap = scaled_bounds[0]  # Set cap to the smallest scaled bound
    
    # Compute sum recursively
    rest = sum(coprime_count(divisor * d) for d in range(2, cap + 1))  # Sum over all possible divisors
    
    # Store result in cache and return
    cache[divisor] = (total - rest) % (10 ** 9 + 7)  # Store result in cache with modulo operation
    return cache[divisor]
    
# Read number of test cases
t = int(input())  
for _ in range(t):
    k = int(input())  # Read k value
    bounds = list(map(int, input().split()))  # Read bounds and convert to list of integers
    bounds.sort()  # Sort bounds in ascending order
    cache = dict()  # Initialize cache as an empty dictionary
    total = 0  # Initialize total sum
    
    # Iterate from 1 to smallest bound and compute total sum
    for i in range(1, bounds[0] + 1):  
        total = (total + i * coprime_count(i)) % (10 ** 9 + 7)  # Compute and update total sum
    
    print(total)  # Print final result
