# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

# Read the number of lists (k) and the modulo value (m)
k, m = map(int, input().split())

# Initialize an empty list to hold all input lists
lists = []

# Read k lists and append them to the `lists` variable (excluding the first number in each line)
for i in range(k):
    lists.append(list(map(int, input().split()))[1:])

# Generate all possible combinations (Cartesian product) of the lists
comb = list(itertools.product(*lists))

# Define a function to calculate the modular sum of squares
def fon(x):
    s = 0
    for ele in x:
        s += ele ** 2  # Square each element and add it to the sum
    s %= m  # Take the sum modulo m
    return s

# Apply the function `fon` to all combinations and store the results
read = list(map(fon, comb))

# Print the maximum value from the results
print(max(read))