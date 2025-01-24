# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

# Read and process the input
s = input().split()
st = ''.join(sorted(s[0]))  # Sort the string alphabetically
k = int(s[1])  # Length of permutations

# Generate all permutations of length k
l = list(permutations(st, k))

# Print each permutation
for ele in l:
    for nb in ele:
        print(nb, end='')  # Print each character without a space
    print('')  # Move to the next line after printing each permutation