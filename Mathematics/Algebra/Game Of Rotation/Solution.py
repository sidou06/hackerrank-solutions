# Read number of elements
n = int(input())

# Read list of integers
a = list(map(int, input().split()))

# Initialize weighted sum
somme = 0

# Calculate initial weighted sum
for k in range(n):
    somme += ((k + 1) * a[k])

# Store initial weighted sum as max
pmean = somme

# Calculate total sum of array
total = sum(a)

# Iterate through n - 1 rotations
for j in range(n - 1):
    # Update weighted sum for rotation
    somme -= total 
    somme += n * a[j]
    # Update max weighted sum if needed
    if somme > pmean:
        pmean = somme 

# Print maximum weighted sum
print(pmean)