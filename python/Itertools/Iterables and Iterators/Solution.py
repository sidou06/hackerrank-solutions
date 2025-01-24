# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

# Read the input values
n = int(input())  # Length of the list
lis = input().split()  # List of elements
k = int(input())  # Length of combinations

cpt = 0  # Counter for combinations containing 'a'
# Generate all combinations of length k
a = list(combinations(lis, k))

# Count the combinations containing 'a'
for ele in a:
    if 'a' in ele:
        cpt += 1

# Calculate and print the probability
print(cpt / len(a))