# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

# Read input string
s = input()

# Group consecutive identical characters
data = groupby(s)

# Initialize a list to store the tuples
tuples = []

# Iterate through each group
for char, rep in data:
    val = str(len(''.join(rep)))  # Count the occurrences of the character
    c = "(" + val + ", " + char + ")"  # Format the output as a tuple
    tuples.append(c)

# Print the tuples separated by spaces
print(" ".join(ele for ele in tuples))