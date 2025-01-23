# Enter your code here. Read input from STDIN. Print output to STDOUT

# Initialize an empty set to store unique elements
s = set()

# Read the number of elements to be added to the set
n = int(input().rstrip())

# Loop through the input and add each element to the set
for i in range(n):
    s.add(input().rstrip())

# Print the number of unique elements in the set
print(len(s))