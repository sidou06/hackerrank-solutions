# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement as co

# Read and process the input
inp = input().rstrip().split()
# Generate combinations with replacement and sort the characters
s = list(co(sorted(inp[0]), int(inp[1])))

# Iterate through each combination
for ele in s:
    r = ""  # Initialize an empty string for the combination
    for k in range(int(inp[1])):  # Concatenate each character in the combination
        r += ele[k]
    print(r)  # Print the combination